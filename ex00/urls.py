from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('init/', views.ok_sql, name='sql_page'),
]