from django.urls import path
from education import views

app_name = 'education'

urlpatterns = [
    path('education_index',views.education_index,name='education_index'),
    path('comp_sci',views.comp_sci,name='comp_sci'),
    path('cog_sci',views.cog_sci,name='cog_sci'),
    path('class_history',views.class_history,name='class_history'),
    path('tech_dets',views.tech_dets,name='tech_dets'),

]
