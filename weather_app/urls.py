from django.urls import path

from weather_app import views

app_name = 'weather_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),

    path('place/<int:_id>', views.place_data, name='place'),
    path('delete/<int:_id>', views.place_delete, name='delete'),
]
