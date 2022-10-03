from tkinter import CASCADE
from unicodedata import category, name
from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name



class Question(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    question = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.question


class Answer(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.answer



