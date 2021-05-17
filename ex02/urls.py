from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('init/', views.create_db, name='create_sql'),
    url('populate/', views.populate_data, name='populate'),
    url('display/', views.display_data, name='display'),
]