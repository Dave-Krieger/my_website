from django.urls import path
from data_viz import views

app_name = 'data_viz'

urlpatterns = [
    path('data_viz_index',views.data_viz_index,name='data_viz_index'),
    path('temperature',views.temperature,name='temperature'),
    path('co2',views.co2,name='co2'),
    path('data_wrangle',views.data_wrangle,name='data_wrangle'),
    path('tech_dets',views.tech_dets,name='tech_dets'),

]
