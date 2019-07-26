from django.contrib import admin
from psql_db.models import School,Student
# Register your models here.
admin.site.register(School)
admin.site.register(Student)
