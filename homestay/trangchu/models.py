from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Phong(models.Model):
    Ten = models.CharField(max_length=200, null=True)
    Diachi = models.CharField(max_length=200, null=True)
    Netflix = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Beprieng = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Bontam = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Diachi = models.CharField(max_length=200, null=True)
    Hinhanh =models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.Ten
    @property
    def HinhanhURL(self):
        try:
            url= self.Hinhanh.url
        except:
            url=''
        return url
class Giohang(models.Model):
    date_oder = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
class Giohang_items(models.Model):
    phong = models.ForeignKey(Phong, on_delete=models.SET_NULL, blank=True, null=True)
    giohang = models.ForeignKey(Giohang, on_delete=models.SET_NULL, blank=True, null=True)
    soluong = models.IntegerField(default=0,null=True, blank=True)
    gia = models.IntegerField(null=True)

    def __str__(self):
        return self.giohang
class Banggia(models.Model):
    phong = models.ForeignKey(Phong, on_delete = models.SET_NULL, blank=True, null=True)
    Gia4tieng = models.IntegerField(null = True, blank=True)
    Gia20h_9h = models.IntegerField( blank=True, null=True)
    Gia10h_19h = models.IntegerField(blank=True, null=True)
    Gia14h_12h = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.phong.id)

