from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=100, primary_key=True)

class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE )
    author = models.CharField(max_length=50)
    date = models.DateField()

# Create your models here.
