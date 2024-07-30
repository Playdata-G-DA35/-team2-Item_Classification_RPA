from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/delete/', views.photo_delete, name='photo_delete'),
    path('upload/', views.photo_upload, name='photo_upload'),
    path('top_reviews/', views.top_reviews, name='top_reviews'), 
]
