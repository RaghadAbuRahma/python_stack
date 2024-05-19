from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=45)
    Network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    