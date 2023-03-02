from django.urls import path 
from . import views

urlpatterns = [
    path('', views.catmed_list),
    path('<int:pk>/', views.catmed_detail),
]
