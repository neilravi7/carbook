from django.urls import path
from . import views 
# AUTHENTICATION VIEWS

app_name = 'vehicle'

urlpatterns=[
    path('list/', views.VehicleAPIList.as_view(), name='vehicle_list'),
    path('<int:pk>/detail/', views.VehicleAPIDetail.as_view(), name='vehicle_detail'),
    path('<int:pk>/admin', views.VehicleAPIAdminView.as_view(), name='vehicle_admin'),
]

