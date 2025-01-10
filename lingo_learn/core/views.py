from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    return Response(data="Hello World", status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTest(request):
    """Returns a collection of questions."""

    questions = {'question1':'How do you say hello in Spanish?'}
    data = questions

    return Response(data=data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gradeTest(request):
    """Grades test and returns a lesson based on the score."""

    answers = {'answer1':'hola'}
    grade = 0
    lesson = ''

    if request.data.get('answer1') == answers.get('answer1').lower():
        grade = 1

    # if user received good grade, give them an advanced lesson, otherwise, give them a beginner lesson
    if grade == 1:
        lesson = {'difficulty': 'advanced', 'subject': 'Spanish', 'contents':'Some advanced lesson about the Spanish language.'}
    elif grade == 0:
        lesson = {'difficulty': 'beginner', 'subject': 'Spanish', 'contents':'Some beginner lesson about the Spanish language.'}

    return Response(data=lesson, status=200)