from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField()
    title = models.CharField(max_length=300)

class Question(models.Model):
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to ='uploads/question_img/')

class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)