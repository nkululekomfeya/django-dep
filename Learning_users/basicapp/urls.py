from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'basicapp'

urlpatterns=[
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
]
