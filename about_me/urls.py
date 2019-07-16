from django.urls import path
from about_me import views

app_name = 'about_me'

urlpatterns = [
    path('about_me_index',views.about_me_index,name='about_me_index'),
    path('hobbies',views.hobbies,name='hobbies'),
    path('class_history',views.class_history,name='class_history'),
    path('comp_sci',views.comp_sci,name='comp_sci'),
    path('cog_sci',views.cog_sci,name='cog_sci'),
    path('tech_dets',views.tech_dets,name='tech_dets'),

]
