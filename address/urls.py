from django.urls import path

from address.views import AddressesAPIView

urlpatterns = [
    path('addresses/', AddressesAPIView.as_view()),
    path('addresses/<int:address_id>/', AddressesAPIView.as_view()),
]