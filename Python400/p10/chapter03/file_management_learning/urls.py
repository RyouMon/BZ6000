from django.urls import path
from . import views


app_name = 'file_management_learning'

urlpatterns = [
    path('photos/<int:pk>/', views.get_photo, name='show_photos'),
]
