from django.urls import path
from main_page import views
from data_viz import views as data_viz_views

app_name = 'main_page'

urlpatterns = [
    path('index',views.index,name='index'),
    path('data_viz_index',data_viz_views.data_viz_index,name='data_viz_index'),
]
