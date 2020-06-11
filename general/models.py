from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class Team(models.Model):
    ConferenceSide = models.TextChoices('ConferenceSide', 'WESTERN EASTERN')
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    city = models.CharField(max_length=255,unique=True)
    arena  = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True,default='')
    logo = models.ImageField(upload_to='media')
    wins = models.IntegerField()
    looses = models.IntegerField()
    conference = models.CharField(blank=True, choices=ConferenceSide.choices, max_length=30)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-wins']

class Player(models.Model):
    name = models.CharField(max_length=255,unique=True)
    surname = models.CharField(max_length=255,unique=True)
    team = models.ForeignKey(Team,related_name='team_related',on_delete=models.CASCADE)
    height = models.FloatField()
    age = models.IntegerField()
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    photo = models.ImageField(upload_to='media',default='')

    def __str__(self):
        return self.surname

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name + self.surname)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('general:team',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['surname']
