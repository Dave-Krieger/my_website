from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                    ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from . import models

class psql_index(TemplateView):
    template_name = 'psql_db/index.html'

class tech_dets(TemplateView):
    template_name = 'psql_db/tech_dets.html'
#--------------------------------------------------------
# School Views
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'psql_db/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal', 'location')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("psql_db:listSchool")

#----------------------------------------------------#
#Student Views

class StudentListView(ListView):
    context_object_name = 'students'
    model = models.Student

class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.Student
    template_name = 'psql_db/student_detail.html'

class StudentCreateView(CreateView):
    fields = ('name','age', 'school')
    model = models.Student

class StudentUpdateView(UpdateView):
    fields = ('name','age', 'school')
    model = models.Student

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("psql_db:listStudent")
