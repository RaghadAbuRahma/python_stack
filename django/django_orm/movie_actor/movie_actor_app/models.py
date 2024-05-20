from django.db import models





class Actor(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model): 
    name = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    url_image = models.TextField()
    actor = models.ManyToManyField(Actor, related_name='movies')
    category = models.ForeignKey(Category, related_name="movies", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






    