from django.db import models
from django.db.models import CharField, FloatField, ForeignKey, UniqueConstraint, Manager, BooleanField

from auth_jwt.models import User


class AddressManager(Manager):
    def get_by_id(self, address_id, owner):
        try:
            return self.model.objects.filter(id=address_id, owner=owner).first()
        except self.model.DoesNotExist:
            return None


class Address(models.Model):
    class Meta:
        constraints = [UniqueConstraint(fields=['owner', 'source'], name='unique_address')]

    objects = AddressManager()

    owner = ForeignKey(User, on_delete=models.CASCADE)
    source = CharField(max_length=250)
    edited = BooleanField(default=False)
    postal_code = CharField(max_length=6, null=True)
    country = CharField(max_length=120)
    federal_district = CharField(max_length=20, null=True)
    region = CharField(max_length=120, null=True)
    area = CharField(max_length=120, null=True)
    city = CharField(max_length=120, null=True)
    city_district = CharField(max_length=120, null=True)
    settlement = CharField(max_length=120, null=True)
    street_type_full = CharField(max_length=50, null=True)
    street = CharField(max_length=120, null=True)
    stead = CharField(max_length=50, null=True)
    house = CharField(max_length=50, null=True)
    block = CharField(max_length=50, null=True)
    entrance = CharField(max_length=10, null=True)
    floor = CharField(max_length=10, null=True)
    flat = CharField(max_length=50, null=True)
    geo_lat = FloatField()
    geo_lon = FloatField()
