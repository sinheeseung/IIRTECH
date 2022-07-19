from django.db import models


# class Recipe(models.Model):
#         name = models.CharField(max_length=100)
#         country = models.CharField(max_length=100)
#         ingredient = models.TextField()
#
#         def __str__(self):
#                 return self.name

class Recipe(models.Model):
    object = models.Manager()
    word = models.TextField()
    sense_no = models.TextField()
    primary_key = models.TextField()

