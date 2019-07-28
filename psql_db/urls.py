from django.urls import path, re_path, include
from psql_db import views

app_name = 'psql_db'

urlpatterns = [
    path('psql_index',views.psql_index.as_view(),name='psql_index'),

    re_path(r'^listSchool/$', views.SchoolListView.as_view(), name='listSchool'),
    re_path(r'^listSchool/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detailSchool'),
    re_path(r'^createSchool/$', views.SchoolCreateView.as_view(), name='createSchool'),
    re_path(r'^updateSchool/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='updateSchool'),
    re_path(r'^deleteSchool/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='deleteSchool'),

    re_path(r'^listStudent/$', views.StudentListView.as_view(), name='listStudent'),
    re_path(r'^listStudent/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detailStudent'),
    re_path(r'^createStudent/$', views.StudentCreateView.as_view(), name='createStudent'),
    re_path(r'^updateStudent/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='updateStudent'),
    re_path(r'^deleteStudent/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='deleteStudent'),

    path('tech_dets',views.tech_dets.as_view(),name='tech_dets'),

]
