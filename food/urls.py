from django.urls import path
from food import views

urlpatterns = [
    path('', views.food_index, name="food_index"),
    path('category/<int:pk>/', views.food_cat, name="food_cat")
]
