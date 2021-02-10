from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ActivityPeriode(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Member(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length = 50)
    tz = models.CharField(max_length=50)
    activity_periode = models.ForeignKey(ActivityPeriode, on_delete=models.CASCADE)




