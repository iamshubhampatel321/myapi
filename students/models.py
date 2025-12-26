from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    college_name = models.CharField(max_length=150)
    roll_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
