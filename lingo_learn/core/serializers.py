from rest_framework.serializers import ModelSerializer
from .models import User, Test, Question, Choice, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['user', 'difficulty', 'subject', 'contents']

class UserSerializer(ModelSerializer):
    lessons = LessonSerializer(many=False, read_only=True)
    class Meta:

        model = User
        fields = ['first_name', 'username']

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
        fields = ['id','difficulty', 'title', 'questions']