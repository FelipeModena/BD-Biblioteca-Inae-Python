from django.urls import path

from pessoas import views

urlpatterns = [
    path('pessoas/', views.pessoas),
]
