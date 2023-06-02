from django.db import models
import datetime

from django.db import models
import datetime

class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, default='', null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def age(self):
        return int((datetime.date.today() - self.date_of_birth).days / 365.25)
    
    def __str__(self):
        return self.name
    

    def age(self):
        return int((datetime.date.today() - self.date_of_birth).days / 365.25)
    
    def __str__(self):
        return self.name
    
