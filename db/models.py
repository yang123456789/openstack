from django.db import models


class Register(models.Model):
    auth_token = models.CharField(max_length=255, null=False)
    register_time = models.DateTimeField(auto_now_add=True)
    customer_username = models.CharField(max_length=255, null=False, db_index=True)
    customer_phone = models.CharField(max_length=255, null=False)
    customer_password = models.CharField(max_length=255, null=False)
    customer_again_password = models.CharField(max_length=255, null=False)
    identify_code = models.CharField(max_length=255, null=False)

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (
            self.auth_token,
            self.register_time,
            self.customer_username,
            self.customer_phone,
            self.customer_password,
            self.customer_again_password,
            self.identify_code
        )

# Create your models here.
