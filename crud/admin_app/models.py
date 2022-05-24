from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    

    class Meta:
        db_table="student"