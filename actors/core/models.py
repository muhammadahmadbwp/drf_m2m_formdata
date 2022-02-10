from django.db import models
from django.utils import timezone
import os

# Create your models here.


class ActorsDetail(models.Model):

    name = models.CharField(max_length=100)
    dob = models.DateField()
    spouse = models.CharField(max_length=100, null=True, blank=True)
    children = models.ManyToManyField('core.Children', blank=True, related_name='children')
    pictures = models.ManyToManyField('core.Pictures', blank=True, related_name='pictures')
    movies = models.ManyToManyField('core.Movies', blank=True, related_name='movies')

class Children(models.Model):

    name = models.CharField(max_length=100)
    dob = models.DateField()


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"actors/{base}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class Pictures(models.Model):

    pic = models.ImageField(upload_to=upload_to, blank=True, null=True)


class Movies(models.Model):

    name = models.CharField(max_length=100)
    budget_usd = models.IntegerField(null=True, blank=True)
    business_usd  = models.IntegerField(null=True, blank=True)
    release_date = models.DateField()

