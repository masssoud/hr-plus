from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        full_name = '{} {}'.format(obj.first_name, obj.last_name)
        if full_name.strip() == '':
            full_name = obj.username
        return full_name.strip()

    class Meta:
        model = get_user_model()
        read_only_fields = ['date_joined', 'last_login', 'is_superuser', 'full_name']
        exclude = ['password']


class CreateUpdateUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    email = serializers.EmailField(
        max_length=None,
        min_length=None,
        allow_blank=False,
        label=_('email address'),
        validators=[
            UniqueValidator(queryset=get_user_model().objects.all(),
                            message=_('A user with this email address already exists.'))]
    )

    def get_full_name(self, obj):
        full_name = '{} {}'.format(obj.first_name, obj.last_name)
        if full_name.strip() == '':
            full_name = obj.username
        return full_name.strip()

    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ['date_joined', 'last_login', 'is_superuser', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        get_user_model()
        if 'email' in validated_data:
            validated_data['email'] = BaseUserManager.normalize_email(validated_data['email'])
        if 'username' in validated_data:
            validated_data['username'] = AbstractUser.normalize_username(validated_data['username'])
        user = super(CreateUpdateUserSerializer, self).update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        user.save()
        return user

    def updatePassword(self, data, user):
        user.set_password(data)
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        full_name = '{} {}'.format(obj.first_name, obj.last_name)
        if full_name.strip() == '':
            full_name = obj.username
        return full_name.strip()

    class Meta:
        model = get_user_model()
        fields = ['id', 'full_name', 'is_active', 'date_joined', 'is_staff', 'url', 'full_name']
        read_only_fields = ['date_joined', 'last_login', 'is_superuser']
