from django.db import models


class Animals(models.Model):
    name = models.CharField(max_length=1000)


animal1 = Animals()

animal1.name = 'Panda'

print(animal1)
