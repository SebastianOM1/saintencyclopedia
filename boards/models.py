from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User
from partial_date import PartialDateField


# Create your models here.
class Saint(models.Model):
    name = models.CharField(max_length=50)
    birthDateType = models.CharField(max_length=20, blank=True, null=True)
    birthDate = PartialDateField(null=True)
    birthCity = models.CharField(max_length=30, blank=True, null=True)
    birthCountry = models.CharField(max_length=50, blank=True, null=True)
    deathDateType = models.CharField(max_length=20, blank=True, null=True)
    deathDate = PartialDateField(null=True)
    deathCity = models.CharField(max_length=30, blank=True, null=True)
    deathCountry = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    art = models.FileField(default='unknown.png')
    
    def __str__(self):
        return self.name
    
class Miracle(models.Model):
    performedBy = models.ForeignKey(Saint, related_name='miracles', on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    addedBy = models.ForeignKey(User, related_name='miracle_contributions', on_delete=models.CASCADE)
    addedOn = models.DateTimeField(auto_now_add=True)
    isConfirmed = models.BooleanField(default=False)
    
class Artwork(models.Model):
    depicting = models.ForeignKey(Saint, related_name='artworks', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    artist = models.CharField(max_length=70)
    creationDate = models.DateField(null=True)
    uploadedBy = models.ForeignKey(User, related_name='artwork_contributions', on_delete=models.CASCADE)
    uploadedOn = models.DateTimeField(auto_now_add=True)
    image = models.FileField()
    
class Prayer(models.Model):
    of = models.ForeignKey(Saint, related_name='prayers', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    addedBy = models.ForeignKey(User, related_name='prayer_contributions', on_delete=models.CASCADE)
    addedOn = models.DateTimeField(auto_now_add=True)