from django.urls import path

from weather_app import views

urlpatterns = [
    path('admin/', views.index, name='index'),
]
