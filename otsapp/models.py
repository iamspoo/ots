from django.db import models

class customer(models.Model):
    customer_id=models.AutoField
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=5)
    password=models.CharField(max_length=15)



class order(models.Model):
    orderid=models.CharField(max_length=10)
    name=models.CharField(max_length=30)
    status=models.CharField(max_length=25)
