from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if self.objects.count() > 0:
            pass
        else:
            return super(Contact, self).save(*args, **kwargs)




