from django.urls import path
from emprestimos import views

urlpatterns = [
    path('emprestimos/', views.emprestimos),
]
