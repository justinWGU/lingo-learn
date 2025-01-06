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