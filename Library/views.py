from hashlib import sha256

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import BookModel
from .models import AuthorModel
from .Serializer import BookSerializer, IsStaff
from .Serializer import AuthorSerializer


# Create your views here.
class BooksView(APIView, UpdateModelMixin, DestroyModelMixin):

    permission_classes = [IsStaff]
    @staticmethod
    def get(request, id=None):
        if id:
            try:
                querySet = BookModel.objects.get(id=id)
            except BookModel.DoesNotExist:
                return Response({"msg": "Book Not Found"}, status=403)

            SerializedBook = BookSerializer(querySet)
        else:
            querySet = BookModel.objects.all()

            SerializedBook = BookSerializer(querySet, many=True)

        return Response(SerializedBook.data, status=200)


    @staticmethod
    def post(request):
        create_serializer = BookSerializer(data=request.data)

        if create_serializer.is_valid():
            new_book = create_serializer.save()
            serialized_new_book = BookSerializer(new_book)

            return Response(serialized_new_book.data, status=201)
        return Response({"msg": "Invalid Data"}, status=400)

    @staticmethod
    def put(request, id=None):
        try:
            book = BookModel.objects.get(id=id)
        except BookModel.DoesNotExist:
            return Response({"msg": "Book with Id Not Found"})

        book_serialized = BookSerializer(book, data=request.data)
        if book_serialized.is_valid():
            updated_book = book_serialized.save()
            serialized_updated_book = BookSerializer(updated_book)
            return Response(serialized_updated_book.data, status=200)

        return Response({"msg": "Invalid Data"})


    @staticmethod
    def delete(request, id=None):
        try:
            book = BookModel.objects.get(id=id)
        except:
            return Response({"msg": "Book with Id Not Found"})

        book.delete()
        return Response({"msg": "book deleted Successfully"}, status=403)




class AuthorView(APIView, UpdateModelMixin, DestroyModelMixin):

    permission_classes = [IsStaff]
    @staticmethod
    def get(request, id=None):
        if id:
            try:
                querySet = AuthorModel.objects.get(id=id)
            except AuthorModel.DoesNotExist:
                return Response({"msg": "Author Not Found"}, status=403)

            SerializedAuthor = AuthorSerializer(querySet)
        else:
            querySet = AuthorModel.objects.all()

            SerializedAuthor = AuthorSerializer(querySet, many=True)

        return Response(SerializedAuthor.data, status=200)


    @staticmethod
    def post(request):
        create_serializer = AuthorSerializer(data=request.data)

        if create_serializer.is_valid():
            new_book = create_serializer.save()
            serialized_new_auhtor = AuthorSerializer(new_book)

            return Response(serialized_new_auhtor.data, status=201)
        return Response({"msg": "Invalid Data"}, status=400)

    @staticmethod
    def put(request, id=None):
        try:
            Author = AuthorModel.objects.get(id=id)
        except AuthorModel.DoesNotExist:
            return Response({"msg": "Author with Id Not Found"})

        author_serialized = AuthorSerializer(Author, data=request.data)
        if author_serialized.is_valid():
            updated_author = author_serialized.save()
            serialized_updated_author = AuthorSerializer(updated_author)
            return Response(serialized_updated_author.data, status=200)

        return Response({"msg": "Invalid Data"})

    @staticmethod
    def delete(request, id=None):
        if not AuthorModel.objects.filter(id=id).exists():
            return Response({"msg": "Author with Id Not Found"})

        author = AuthorModel.objects.get(id=id)

        author.delete()
        return Response({"msg": "Author deleted Successfully"}, status=403)


