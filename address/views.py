from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from address.exceptions import AddressValidationException
from address.models import Address
from address.serializers import AddressCreateSerializer, AddressUpdateSerializer
from address.services import AddressesService


class AddressesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressCreateSerializer
    serializer_update_class = AddressUpdateSerializer
    model = Address
    address_service = AddressesService()

    def get(self, request):
        addresses = self.model.objects.filter(owner=request.user.id)
        if not addresses:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        query = request.data.get('address', None)
        if query is None:
            return Response('Empty data', status=status.HTTP_400_BAD_REQUEST)
        try:
            data = self.address_service.validate_address(query)
        except AddressValidationException as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, address_id):
        address = self.model.objects.get_by_id(address_id=address_id, owner=request.user.id)
        if address is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data.get('address', None)
        serializer = self.serializer_update_class(address, data=data)
        if serializer.is_valid():
            serializer.save(edited=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, address_id):
        address = self.model.objects.get_by_id(address_id=address_id, owner=request.user.id)
        if address is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
