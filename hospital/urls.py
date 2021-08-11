from django.urls import path
from .views import (AppointmentListView, AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView,)



urlpatterns = [
    path('', AppointmentListView.as_view(), name= 'appointment_list'),
    path('appointment/create', AppointmentCreateView.as_view(), name='appointment_create'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name= 'appointment_detail'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),

]

