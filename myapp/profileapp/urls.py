
from django.urls import path
from .views import profile_detail, profile_create

urlpatterns = [
    path('create/<int:user_id>/', profile_create, name='profile_create'),
    path('view/<int:user_id>/', profile_detail, name='profile_detail'),
]
