from django.db import models

class Student(models.Model):
    admin_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    classes = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    fingerPrint = models.CharField(max_length=4)
    photo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.admin_number
