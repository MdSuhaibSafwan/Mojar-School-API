from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MojarSchoolMember(models.Model):
    SUBSCRIPTION_CHOICES = [
	["MO", "MONTHLY"],
	["QU", "QUARTERLY"],
	["WE", "WEEKLY"],
	["YE", "YEARLY"],
	["DA", "DAILY"],
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_guest = models.BooleanField(default=True)
    subscription = models.CharField(max_length=2, choices=SUBSCRIPTION_CHOICES, null=True)
    company_name = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    street_address = models.TextField(null=True)
    town = models.CharField(max_length=50, null=True)
    post_code = models.CharField(max_length=4, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.email


class MojarSchoolTransaction(models.Model):
    member = models.ForeignKey(MojarSchoolMember, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()

    def __str__(self):
        return str(self.id)
