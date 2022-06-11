from django.urls import path

from weather_app import views

app_name = 'weather_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:_id>', views.place_delete, name='delete'),
    path('place/<int:_id>', views.place_data, name='place'),
]
