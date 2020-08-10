from django.urls import path
from .import views


urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('contactPage/', views.contactPage, name='contactPage'),
    path('AboutPage/', views.AboutPage, name='AboutPage'),
    
]
