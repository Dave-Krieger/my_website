from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length = 128)
    location = models.CharField(max_length = 256)

    def __str__(self):
        return(self.name)

    def get_absolute_url(self):
        return reverse("psql_db:detailSchool", kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length = 128)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students', blank=True,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return(self.name)

    def get_absolute_url(self):
        return reverse("psql_db:detailStudent", kwargs={'pk':self.pk})
