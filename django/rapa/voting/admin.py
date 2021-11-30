from django.contrib import admin
from voting.models import VoteQuestion, VoteChoice

# Register your models here.
admin.site.register(VoteQuestion)
admin.site.register(VoteChoice)