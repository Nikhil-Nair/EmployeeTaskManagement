from django.db import models
from django.contrib.auth.models import  User

#Db model to store task Data
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    task_name = models.CharField(max_length = 100)
    task_description = models.CharField(max_length = 200)
    task_due = models.DateTimeField()
