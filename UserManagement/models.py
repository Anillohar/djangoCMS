from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core import validators
from django import forms
from django.core.exceptions import ValidationError


class AddNewUser(models.Model):
    FullName = models.CharField(max_length=150)
    Email = models.EmailField(max_length=70)
    Username = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField(editable=True)
    ProfileImage =models.ImageField(upload_to='home/Downloads/')
    AddressLine1 = models.CharField(max_length=200)
    AddressLine2 = models.CharField(max_length = 200)
    City = models.CharField(max_length=30)
    State =  models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Zip  =  models.IntegerField(editable=True)
    CreatedOn = models.DateTimeField(default=timezone.now)
    Active = models.BooleanField(default=1)


    def clean_fields(self, exclude=None):
        if exclude is None:
            exclude = []
        errors = {}
        for f in self._meta.fields:
            if f.name == 'Username':
                if len(self.Username)!=0:
                    if (' ' in self.Username):
                      errors[f.name] = [u'No spaces are allowed in Username.']
                    if ( len(self.Username)<5):
                      errors[f.name] = [u'Username must be of 5 characters minimum']
            if f.name == 'PhoneNumber':
                if len(str(self.PhoneNumber)) > 1 :
                    if type(self.PhoneNumber) != int:
                        errors[f.name] = [u'Enter integers only.']


        if errors:
            raise ValidationError(errors)