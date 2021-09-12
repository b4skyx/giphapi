from django.urls import path
from tags import views

urlpatterns = [
    path('', views.tagView),
]
