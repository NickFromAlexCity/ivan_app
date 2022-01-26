from .models import *
from rest_framework import serializers
from rest_framework.response import Response
import datetime


class RetrSer(serializers.Serializer):
    street = serializers.CharField()


class ListSer(serializers.ModelSerializer):

    city = serializers.SerializerMethodField()
    street = serializers.SerializerMethodField()

    def get_city(self, obj):
        return obj.city.city

    def get_street(self, obj):
        return obj.street.street

    class Meta:
        model = Shop
        fields = ("name", "city", "street")


class ShopMS(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'city', 'street')

    def save(self, validated_data):
        "Не допускаем дубликатов"
        shop, created = Shop.objects.get_or_create(**validated_data)
        return shop


class CityMS(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city',)

    def save(self, validated_data):
        "Не допускаем дубликатов"
        city, created = City.objects.get_or_create(**validated_data)
        return city


class StreetMS(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = ('street', 'city',)

    def save(self, validated_data):
        "Не допускаем дубликатов"
        street, created = Street.objects.get_or_create(**validated_data)
        return street



