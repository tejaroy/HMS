from django.urls import path, include
from .views import UsersApp, LoginApi

urlpatterns = [
    path('users/', UsersApp.as_view(), name='users'),
    path('users/<str:phone>', UsersApp.as_view(), name= 'users_edit'),

    path('login/', LoginApi.as_view(), name='login'),
]