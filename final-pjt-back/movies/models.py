from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50)
    overview=models.TextField()
    genre=models.ManyToManyField("movies.Genre")
    rate=models.IntegerField()
    popularity=models.IntegerField()
    release_date=models.DateField()
    poster_path=models.CharField(max_length=50)
    tmdb_id = models.IntegerField()
    # trailer=models.CharField(max_length=50)
    # director=models.CharField(max_length=50)

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)