from django.urls import path
from . import views


urlpatterns = [

    path('nova/', views.home, name='home'),

]