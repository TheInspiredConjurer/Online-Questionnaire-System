from rest_framework import serializers

from .models import User, Role


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "full_name",
            "password",
            "address",
            # "role",
        )

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.full_name = validated_data.get(
            "full_name",
            instance.full_name
        )
        instance.password = validated_data.get("password", instance.password)
        instance.address = validated_data.get(
            "address",
            instance.address
        )
        instance.save()

        return instance


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
        )


class RoleSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="user.role")

    class Meta:
        model = Role
        fields = (
            "id",
            "role",
            "user"
        )
