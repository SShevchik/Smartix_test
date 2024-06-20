from rest_framework.serializers import ModelSerializer

from address.models import Address


class AddressCreateSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['owner']

    def create(self, validated_data):
        instance, _ = self.Meta.model.objects.get_or_create(**validated_data)
        return instance


class AddressUpdateSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['owner', 'source', 'country', 'geo_lat', 'geo_lon']
