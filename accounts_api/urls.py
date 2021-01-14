from django.urls import path
from .views import CustomerList, CustomerDetail

app_name = 'accounts_api'

urlpatterns = [
    path('<int:pk>/', CustomerDetail.as_view(), name='detail'),
    path('', CustomerList.as_view(), name='list'),
]