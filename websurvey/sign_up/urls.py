from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('sign', views.sign, name='sign'),
    path('lending', views.index, name='lending'),


]