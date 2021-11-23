from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='lending'),
    path('sign', views.sign, name='sign'),
    path('login', views.login, name='login')
]