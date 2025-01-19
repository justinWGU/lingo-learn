from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Test, Lesson, Choice, Question
from . import serializers


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    return Response(data="Hello World", status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTest(request):
    """Returns a Test with multiple Questions."""

    language = request.query_params.get('language')
    test = Test.objects.get(language=language)
    serialized_test = serializers.TestSerializer(test)

    return Response(data=serialized_test.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gradeTest(request):
    """Grades test and returns a lesson based on the score."""

    # get the set of questions & answers returned
    questions = request.data.get('questions')
    test_id = request.data.get('test_id')
    total_questions = Test.objects.get(id=test_id).questions.count()

    grade = 0
    score = 0
    for i in range(len(questions)):
        question_id = questions[i].get('question_id')
        answer = questions[i].get('answer')
        correct_answer = Question.objects.get(id=question_id).correct_answer
        if answer == correct_answer:
            score += 1
    grade = score //  total_questions



    # if user received good grade, give them an advanced lesson, otherwise, give them a beginner lesson
    if grade > 0:
        # lesson = {'difficulty': 'advanced', 'subject': 'Spanish', 'contents':'Some advanced lesson about the Spanish language.'}
        lesson = Lesson.objects.get(id=2) # this will hold the adv lesson
    else:
        #lesson = {'difficulty': 'beginner', 'subject': 'Spanish', 'contents':'Some beginner lesson about the Spanish language.'}
        lesson = Lesson.objects.get(id=1) # this will hold the beg lesson

    serialized_lesson = serializers.LessonSerializer(lesson)
    return Response(data=serialized_lesson.data, status=200)