from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    # created_by = models.ForeignKey(User)

    def __str__(self):
        return self.name
