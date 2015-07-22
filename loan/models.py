from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Borrower(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()

class Business(models.Model):

    RETAIL = 'RE'
    PROFESSIONAL_SERVICES = 'PS'
    FOOD = 'FOOD'
    ENTERTAINMENT = 'ENT'

    BUSINESS_SECTOR = (
        (RETAIL, 'retail'),
        (PROFESSIONAL_SERVICES, 'Profession Services'),
        (FOOD, 'Food and Drink'),
        (ENTERTAINMENT, 'Entertainment')
    )

    owner = models.ForeignKey(Borrower)
    company_name = models.CharField(max_length=200)
    address = models.TextField()
    registered_number = models.CharField(max_length=8)
    business_sector = models.CharField(max_length=4, choices=BUSINESS_SECTOR)

class Loan(models.Model):
    business = models.ForeignKey(Business)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(10000),
                                                     MaxValueValidator(100000)])
    days = models.PositiveIntegerField()
    reason = models.TextField()
