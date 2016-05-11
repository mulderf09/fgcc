from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

class Cell(models.Model):
    name = models.CharField(max_length=30)
    area = models.CharField(max_length=50)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "cell"
        
    def __str__(self):
        return self.name
        
        
class Role(models.Model):
    description = models.CharField(max_length=30)

    class Meta:
        ordering = ["description"]
        verbose_name_plural = "role"
        
    def __str__(self):
        return self.description
        

class Ministry(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "ministry"
        
    def __str__(self):
        return self.name
        
        
class Kelas(models.Model):
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "kelas"
        
    def __str__(self):
        return self.name         
        
        
class Adult(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    cell_group = models.ForeignKey(Cell, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    mobile_no = models.CharField(max_length=15)
    email = models.CharField("Email address", max_length=30,blank=True)
    date_joined = models.DateField(default = timezone.now)
    date_left = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=20)
    postcode = models.CharField("Post Code",max_length=5)
    state = models.CharField(max_length=30)
    country = CountryField()
    line1 = models.CharField(max_length=30,default="-")
    line2 = models.CharField(max_length=30,default="-")
    line3 = models.CharField(max_length=30,default="-")

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "adult"
        
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
        

class Kid(models.Model):
    GENDER = (
        ('B', 'Boy'),
        ('G', 'Girl'),
    )
    
    adult_id = models.ForeignKey(Adult, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    cell_id = models.ForeignKey(Cell, on_delete=models.CASCADE)
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    gender = models.CharField("Gender", max_length=1, choices=GENDER)
    mobile_no = models.CharField("Mobile no.", max_length=15)
    email = models.CharField("Email address", max_length=30,blank=True)
    date_joined = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "kid"
        
    def __str__(self):
        return self.first_name        
