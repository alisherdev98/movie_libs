from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'phone',
        )
        extra_kwargs = {'password': {'write_only': True}}
