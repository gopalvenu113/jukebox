from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.


class MusicAlbums(models.Model):
    GENRE_CHOICES = [('1', 'Instrumental'), ('2', 'Classical'), ('3', 'POP'), ('4', 'Rock'), ('5', 'Western')]
    album_name = models.CharField(max_length=50, null=False, validators=[MinLengthValidator(5)])
    date_of_release = models.DateTimeField(auto_now_add=True, null=False)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=False, validators=[MinValueValidator(100), MaxValueValidator(1000)])
    description = models.TextField()

    def __str__(self):
        return self.album_name
    
    # def __init__(self, *args, **kwargs):
    #     pass

    # def save(self, *args, **kwargs):
    #     super.save(*args, **kwargs)
    #     pass

class Musicians(models.Model):
    name = models.CharField(null=False, max_length=30, validators=[MinLengthValidator(3)])
    musician_type = models.CharField(max_length=20, null=True)
    albums = models.ManyToManyField(MusicAlbums, blank=True)

    def __str__(self):
        return self.name