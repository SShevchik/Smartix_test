from rest_framework.serializers import ModelSerializer

from auth_jwt.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}
