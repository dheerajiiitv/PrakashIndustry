from django.db import models

class SubscribedUsers(models.Model):
    email = models.EmailField('E-mail',unique=True)


    def __str__(self):
        return self.email

