from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from auth_jwt.models import User
from auth_jwt.serializers import UserSerializer


class RegistrationAPIView(APIView):
    serializer_class = UserSerializer
    model = User

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response('Invalid data', status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    model = User

    def get(self, request, user_id):
        user = self.model.objects.get_user_by_pk(user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        if not (user.is_staff and user.is_superuser):
            return Response(status=status.HTTP_403_FORBIDDEN)
        data = request.data.get('user', None)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = self.model.objects.get_user_by_pk(request.user.id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data.get('user', None)
        serializer = self.serializer_class(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = self.model.objects.get_user_by_pk(request.user.id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
