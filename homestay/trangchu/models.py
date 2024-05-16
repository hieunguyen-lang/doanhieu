import decimal
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, ImageField
# Create your models here.
class Phong(models.Model):
    Ten = models.CharField(max_length=200, null=True)
    Diachi = models.CharField(max_length=200, null=True)
    Netflix = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Beprieng = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Bontam = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Hinhanh =models.ImageField(null=True, blank=True)
    Gia4tieng = models.IntegerField(null = True, blank=True)
    Gia20h_9h = models.IntegerField(null = True, blank=True)
    Gia10h_19h = models.IntegerField(null = True, blank=True)
    Gia14h_12h = models.IntegerField(null = True, blank=True)
    description = models.TextField(max_length =1500, blank=True, null=True)
    tiktokvid = models.CharField(max_length=200, null=True)
    map = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
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


class posts(models.Model):
    title_imgae = models.ImageField(blank=True, null=True)
    title = models.ImageField(blank=True, null=True)

class Order(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    number = models.CharField(max_length=20, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'Order- {str(self.id)}'
class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE, blank=True, null=True)
    checkin = models.DateTimeField(blank=True, null=True)
    checkout = models.DateTimeField(blank=True, null=True)
    price =models.IntegerField(blank=True, null=True)

    def __str__(self):
        return  f'Order items- {str(self.id)}'
    
class customer_info(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250)
    number = models.CharField(max_length=20, blank=True, null=True)

    def  __str__(self):
        return f'customer info- {str(self.id)}'