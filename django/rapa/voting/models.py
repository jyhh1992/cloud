from django.db import models
# from django.db.models.base import Model

# Create your models here.

class VoteQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) :
        return self.question_text

class VoteChoice(models.Model):
    question = models.ForeignKey(VoteQuestion, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text  
