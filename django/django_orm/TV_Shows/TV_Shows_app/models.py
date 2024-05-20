from django.db import models
# from django.utils import timezone
# from datetime import datetime



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "TV show Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Movie'snetwork should be at least 3 characters"

        # current_date = timezone.now().date()
        # if  ['release_date'] > current_date :
        #     errors["release_date"] = "Release date must be in the past."

        return errors
    

class Show(models.Model):
    title = models.CharField(max_length=45)
    Network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    objects = ShowManager()
