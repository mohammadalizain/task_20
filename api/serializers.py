from rest_framework import serializers
from restaurants.models import Restaurant , Item
from django.contrib.auth.models import User


class Userserializers(serializers.ModelSerializer)
    class Meta:
        model = User
        fields = [
            'user_name',
            'first_name',
            'last_name',
            'email',
            ]


class RestaurantListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
written_by = serializers.SerializersMethodField()
User = Userserializers()

    class Meta:
         model = User
        fields = [
            'name',
            'first_name',
            'last_name',
            'email',
            'written_by',
            ]
def get_Items(self, obj):
    Items = Item.objects.filter(restaurant=obj)
    item_list = ItemSerializer(Items, many=True).data
    return item_list

class RestaurantDetailSerializer(serializers.ModelSerializer):
    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'update',
            'delete',
            ]

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]