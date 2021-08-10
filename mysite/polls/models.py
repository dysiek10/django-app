from django.db import models
import datetime
from django.utils import timezone


# modele służą strukturze bazy danych
# każda klasa w modelach, to reprezentacja tabeli


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        # wypisujemy wartość pola
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# tutan mamy połączone relacją jeden do wielu ze względu na foreign key
class Choice(models.Model):
    # on delete.cascade - jak usuniemy question powyższe to kaskadowo usunie się w choice
    # foreing key - dane pochodzące z relacji (z question w tym wypadku)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text




