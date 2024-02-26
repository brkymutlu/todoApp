from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from='todo',unique = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE) 

    def __str__(self):
        return self.todo