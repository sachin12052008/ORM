from django.db import models
from django.contrib import admin
class car(models.Model):
    car_name=models.CharField(max_length=20)
    year=models.IntegerField()
    color=models.CharField(max_length=10)
    registration_no=models.IntegerField(primary_key=True)
    model=models.CharField(max_length=20)
class carAdmin(admin.ModelAdmin):
    list_display=["car_name","year","color","registration_no","model"]