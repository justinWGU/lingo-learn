from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Lesson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    contents = models.TextField(max_length=1000)

    def __str__(self):
        # determines how the object is printed in the django shell & admin
        return self.subject


class Test(models.Model):
    """Holds the initial test to assess language proficiency level."""

    difficulty = models.CharField(max_length=50) # TODO: Change this to choices
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Holds each test question."""

    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    description = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200, null=True)

class Choice(models.Model):
    """Holds an answer choice for each question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    description = models.CharField(max_length=100)

