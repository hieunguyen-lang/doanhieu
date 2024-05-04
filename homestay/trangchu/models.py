from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Phong(models.Model):
    Ten = models.CharField(max_length=200, null=True)
    Diachi = models.CharField(max_length=200, null=True)
    Netflix = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Beprieng = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Bontam = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Hinhanh =models.ImageField(null=True, blank=True)
    Gia4tieng = models.IntegerField(null = True, blank=True)
    Gia20h_9h = models.IntegerField( blank=True, null=True)
    Gia10h_19h = models.IntegerField(blank=True, null=True)
    Gia14h_12h = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Ten
    @property
    def HinhanhURL(self):
        try:
            url= self.Hinhanh.url
        except:
            url=''
        return url

class image_room(models.Model):
    phong = models.ForeignKey(Phong, on_delete=models.SET_NULL, blank=True, null=True)
    image_1 = models.ImageField( blank=True, null=True)
    image_2 = models.ImageField( blank=True, null=True)
    image_3 = models.ImageField( blank=True, null=True)
    image_4 = models.ImageField( blank=True, null=True)
    image_5 = models.ImageField( blank=True, null=True)
    image_6 = models.ImageField( blank=True, null=True)
    image_7 = models.ImageField( blank=True, null=True)
    image_8 = models.ImageField( blank=True, null=True)
    
    def __str__(self) :
        return  str(self.phong.id)
    @property
    def HinhanhURL1(self):
        try:
            url= self.image_1.url
        except:
            url=''
        return url



