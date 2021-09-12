from django.urls import path
from giphy import views

urlpatterns = [
    path('', views.giphView),
]
