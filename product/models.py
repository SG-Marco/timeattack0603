from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=128, default='')

    
class DrinkModel(models.Model):
    class Meta:
        db_table = "drinks"

    name = models.CharField(max_length=128, default='')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    nutrition = models.CharField(max_length=128, default='')
    allergy = models.CharField(max_length=128, default='')


