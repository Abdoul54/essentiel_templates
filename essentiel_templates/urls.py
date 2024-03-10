"""
URL configuration for essentiel_templates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('use_static/', views.view_static, name='view_static'),
    path('variables/', views.view_variables, name='view_variables'),
    path('attributs/', views.view_attributs, name='view_attributs'),
    path('alternative/', views.view_alternative, name='view_alternative'),
    path('boucle/', views.view_boucle, name='view_boucle'),
    path('heritage/', views.view_heritage, name='view_heritage'),
    path('myform_form/', include('myform_form.urls')),
]
