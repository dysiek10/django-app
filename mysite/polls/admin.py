from django.contrib import admin
from .models import Question, Choice

# to jest panel admina

admin.site.register(Question)
admin.site.register(Choice)
