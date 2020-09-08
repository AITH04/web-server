from django.db import models

# Create your models here.
class Web(models.Model):
    email = models.CharField(max_length=30)  # email
    gender = models.CharField(max_length=10)  # gemder
    subject = models.CharField(max_length=20)  # subject
    interested_things = models.CharField(max_length=30)  #interested_tthings
    # cur_state = models.CharField(max_length=30)
    def __str__(self):
        return self.subject