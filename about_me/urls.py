from django.urls import path
from about_me import views

app_name = 'about_me'

urlpatterns = [
    path('about_me_index',views.about_me_index,name='about_me_index'),
    path('hobbies',views.hobbies,name='hobbies'),
    path('leader',views.leader,name='leader'),
    path('programming',views.programming,name='programming'),
    path('tech_dets',views.tech_dets,name='tech_dets'),

]
