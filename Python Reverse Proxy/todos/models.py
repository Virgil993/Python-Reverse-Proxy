from django.db import models

# Create your models here.
class Responses(models.Model):
    body = models.TextField(max_length=700)
    time = models.CharField(max_length=100)
    header = models.TextField(max_length=1000)


class Requests(models.Model):
    time = models.CharField(max_length=100)
    header = models.TextField(max_length=1000)

