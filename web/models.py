from django.db import models
from django import forms

# Create your models here.
class Web(models.Model):

    gender_choice = (
            (0, 'male'),
            (1, 'female'),
    )
    receivername = models.CharField(max_length=30)
    email = models.CharField(max_length=30)  # email
    gender = models.CharField(max_length=30)
    # gender = forms.IntegerField(widget=forms.widgets.RadioSelect(choices=gender_choice,))  # gender
    receiveage = models.CharField(max_length=20)  # subject
    relationship = models.CharField(max_length=30)  #interested_tthings
    # myrange = models.CharField(max_length=30)
    # cur_state = models.CharField(max_length=30)
    def __str__(self):
        return self.receivername