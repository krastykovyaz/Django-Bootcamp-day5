from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('populate/', views.populate_data, name='populate'),
    url('display/', views.display_data, name='display'),
]