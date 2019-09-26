from django.db import models


class People(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    birthday = models.DateField()
    contact = models.IntegerField(null=True)
    your_name = models.CharField(max_length=20, null=True)
    your_email = models.CharField(max_length=20, null=True)
    your_contact = models.IntegerField(null=True)
    images = models.TextField(null=True)

    def __str__(self):
        return "Hey! {0}, wishing you a very Happy Birthday. Wish you a prosperous, joyful and happiness in life " \
               "ahead. \n\n From, {1}".format(self.name, self.your_name)


class Images(models.Model):
    people_id = models.IntegerField()
    image = models.TextField()
