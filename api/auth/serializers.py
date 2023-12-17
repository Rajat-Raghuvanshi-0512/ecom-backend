from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name"]

    def to_representation(self, obj):
        ret = super(UserSerializer, self).to_representation(obj)
        ret.pop("password")
        return ret
