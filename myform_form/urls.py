from django.urls import path

from . import views
urlpatterns = [
    path('signup10_affichage', views.signup10_affichage, name='signup10_affichage'),
]