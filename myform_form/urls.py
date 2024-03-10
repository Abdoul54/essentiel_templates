from django.urls import path

from . import views
urlpatterns = [
    path('signup10_affichage', views.signup10_affichage, name='signup10_affichage'),
    path('signup20_widget', views.signup20_widget, name='signup20_widget'),
    path('signup30_data', views.signup30_data, name='signup30_data'),
    path('signup30_reussi', views.signup30_reussi, name='signup30_reussi'),
    path('signup31_data/', views.signup31_data, name='signup31_data'),
    path('signup31_affichage/', views.signup31_affichage, name='signup31_affichage'),
]