from django.db import models

# Create your models here.

class TodoModel(models.Model):
    titlle = models.CharField(max_length=100)
    memo = models.TextField(max_length=255)
    def __str__(self):
        return self.titlle