from django.db import models


class People(models.Model):
    name = models.TextField()
    email = models.TextField()
    birthday = models.DateField()



class Images(models.Model):
    people_id = models.IntegerField()
    image = models.TextField()
