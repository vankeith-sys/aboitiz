from __future__ import unicode_literals
import logging
import os
from datetime import date, datetime
from django.db import models
from .extras import TimeStampedModel
from django.utils import timezone



def gen_collector():
    import secrets
    low = 100000
    high = 999999
    out = secrets.randbelow(high - low) + low # out = random number from range [low, high)
    return '%s' %(out)

def gen_accountno():
    import secrets
    low = 1827523965
    high = 9999999999
    out = secrets.randbelow(high - low) + low # out = random number from range [low, high)
    return '%s' %(out)

def gen_cashamt():
    import secrets
    low = 1
    high = 9999
    out = secrets.randbelow(high - low) + low # out = random number from range [low, high)
    return '%d' %(out)

def gen_or_no():
    import random, string
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=11))
    return 'F%s' %(x)

class AP_Payment(TimeStampedModel):
    # payment = {
    #     "transaction_date": 20220124,
    #     "collector_code": 100192,
    #     "account_number": 1827523965,
    #     "cash_amount":    1150.00,
    #     "check_amount":   null,
    #     "total_amount":   1150.00,
    #     "check_number":   null,
    #     "or_no":          "F314C2C8D159",
    #     "teller_code":    "U292",
    #     "time":           "23:38:41"
    # }

    transaction_date = models.DateField()
    collector_code = models.CharField(null=True, blank=True, max_length=30)
    account_number = models.CharField(null=True, blank=True, max_length=30)
    cash_amount = models.FloatField(null=True, blank=True)
    check_amount = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True,)
    check_number = models.CharField(null=True, blank=True, max_length=30)
    or_no = models.CharField(null=True, blank=True, max_length=30)     
    teller_code = models.CharField(null=True, blank=True, max_length=30)  
    time = models.TimeField(null=True, blank=True)

    payment_date = models.DateField()
    biller = models.CharField(null=True, blank=True, max_length=30)
    user_id = models.CharField(null=True, blank=True, max_length=30)
    account_id = models.CharField(null=True, blank=True, max_length=30)
    account_name = models.CharField(null=True, blank=True, max_length=30)
    remarks = models.CharField(null=True, blank=True, max_length=30)




