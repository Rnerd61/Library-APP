from rest_framework import serializers

from .models import BookModel
from .models import AuthorModel


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    author = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
        authorName = validated_data.get('author')
        author, created = AuthorModel.objects.get_or_create(name=authorName)
        return BookModel.objects.create(
            name=validated_data.get('name'),
            author=author
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        authorName = validated_data.get('author', instance.author)
        author, created = AuthorModel.objects.get_or_create(name=authorName)

        instance.author = author
        instance.save()

        return instance

    class Meta:
        model = BookModel
        fields = (
            'name',
            'author',
        )


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
        return AuthorModel.objects.create(
            name=validated_data.get('name')
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance

    class Meta:
        model = AuthorModel
        fields = (
            'name',
        )


from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user and request.user.is_staff