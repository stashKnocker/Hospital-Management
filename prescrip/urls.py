from django.urls import path
from .views import (PrescriptionListView, PrescriptionDetailView, PrescriptionUpdateView, PrescriptionCreateView, PrescriptionDeleteView)



urlpatterns = [
    path('',PrescriptionListView.as_view(), name='prescription_list'),
    path('prescription/create',PrescriptionCreateView.as_view(), name='prescription_create'),
    path('<int:pk>/',PrescriptionDetailView.as_view(), name= 'prescription_detail'),
    path('<int:pk>/delete/',PrescriptionDeleteView.as_view(), name='prescription_delete'),
    path('<int:pk>/edit/',PrescriptionUpdateView.as_view(), name='prescription_edit'),
]