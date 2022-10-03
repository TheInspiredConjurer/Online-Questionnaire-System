from django.contrib import admin
from questionnaire.models import Category, Question, Answer

# Register your models here.
admin.site.register((Category,
                    Question,
                    Answer,
                    ))
