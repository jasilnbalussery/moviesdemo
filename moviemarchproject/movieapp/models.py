from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    category = models.TextField()
    date = models.DateField()
    actors = models.TextField()
    trailer_link = models.URLField()
    img = models.ImageField(upload_to='gallery')


    def __str__(self):
        return self.title
