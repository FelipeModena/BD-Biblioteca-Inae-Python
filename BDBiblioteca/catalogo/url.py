from django.urls import path

from catalogo import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
]
