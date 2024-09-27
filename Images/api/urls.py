
from django.urls import path
from . import views


urlpatterns = [
  path('', views.dataView, name='all_data'),
]