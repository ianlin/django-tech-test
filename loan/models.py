from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User

import const

BUSINESS_SECTOR = []
for b in const.BUSINESS_SECTOR:
    BUSINESS_SECTOR.append((const.BUSINESS_SECTOR[b], b))

class Borrower(models.Model):

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()

class Business(models.Model):

    def __str__(self):
        return self.company_name

    def __unicode__(self):
        return self.company_name

    def owner_name(self):
        return self.owner.name

    owner = models.ForeignKey(Borrower)
    company_name = models.CharField(max_length=200)
    address = models.TextField()
    registered_number = models.CharField(max_length=8)
    business_sector = models.CharField(max_length=4, choices=BUSINESS_SECTOR)

class Loan(models.Model):

    def __str__(self):
        return '{0} : {1}'.format(self.business.company_name, self.amount)

    def __unicode__(self):
        return '{0} : {1}'.format(self.business.company_name, self.amount)

    def company_name(self):
        return self.business.company_name

    business = models.ForeignKey(Business)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(10000),
                                                     MaxValueValidator(100000)])
    days = models.PositiveIntegerField()
    reason = models.TextField()
