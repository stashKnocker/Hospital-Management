from django.urls import path
from .views import (ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView,)



urlpatterns = [
    path('', ProfileListView.as_view(), name= 'profile_list'),
    path('profile/create', ProfileCreateView.as_view(), name='profile_create'),
    path('<int:pk>/', ProfileDetailView.as_view(), name= 'profile_detail'),
    path('<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('<int:pk>/edit/',ProfileUpdateView.as_view(), name='profile_edit')
]
