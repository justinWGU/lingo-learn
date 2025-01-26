from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import User, Test, Question, Choice, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['language', 'difficulty', 'subject', 'contents']

class UserSerializer(ModelSerializer):
    #lessons = LessonSerializer(many=False, read_only=True)
    password = serializers.CharField(max_length=50, write_only=True, required=True)

    class Meta:

        model = User
        fields = ['first_name', 'username', 'password']

    def create(self, validated_data):
        # make sure the password gets hashed
        password = validated_data.pop('password', None)

        # save user first regardless of pw
        user = User.objects.create_user(
            **validated_data
        )

        # if pw isn't empty, update the user
        if password is not None:
            user.set_password(password)
            user.save()
        return user


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ['description']

class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id','description', 'choices']

class TestSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = ['id','language','difficulty', 'title', 'questions']