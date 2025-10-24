from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewListCreate.as_view(), name='review-list'),
    path('reviews/delete/<int:pk>/', views.ReviewDelete.as_view(), name='delete-review'),
]