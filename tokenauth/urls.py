from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.authtoken import views
urlpatterns = [
    path('token', obtain_auth_token)
]
