from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=125)
    director = models.CharField(max_length=125)
    release = models.DateField()
    genre = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title