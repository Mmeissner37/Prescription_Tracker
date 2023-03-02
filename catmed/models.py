from django.db import models

class CatMed(models.Model):
    cat_name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    