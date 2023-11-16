from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return f"{self.name} - {self.year} "

class Song(models.Model):
    title = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=4, decimal_places=2)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")


    def __str__(self):
        return self.title


