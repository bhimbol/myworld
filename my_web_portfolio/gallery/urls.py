from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('image/<int:image_id>/', views.add_image_comment, name='add_image_comment'),
]