from django.db import models


class Register(models.Model):
    customer_username = models.CharField(max_length=255, null=False, db_index=True)
    customer_phone = models.CharField(max_length=255, null=False)
    customer_password = models.CharField(max_length=255, null=False)
    customer_again_password = models.CharField(max_length=255, null=False)
    identify_code = models.CharField(max_length=255, null=False)


# Create your models here.
