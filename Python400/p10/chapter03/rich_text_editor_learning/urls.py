from django.urls import path
from . import views


app_name = 'rich_text_editor_learning'

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('add_post/', views.add_view, name='add_post'),
    path('update_post/', views.update_post, name="update_post"),
]
