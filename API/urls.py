from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post_view'),
    path('post/<int:pk>/', views.UpdateDeleteRetrieve.as_view(), name='update_delete_retrieve'),
]