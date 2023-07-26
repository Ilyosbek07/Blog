from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from apps.article.models import Article, Author, Tag, Category, Subscription, Occupation, Instagram, Comment
from apps.article.serializers import ArticleSerializer, AuthorSerializer, TagSerializer, CategorySerializer, \
    SubscriptionSerializer, OccupationSerializer, InstagramSerializer, CommentSerializer


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class InstagramListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = InstagramSerializer
    queryset = Instagram.objects.all()


class InstagramRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstagramSerializer
    queryset = Instagram.objects.all()


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class TagListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubscriptionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class OccupationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OccupationSerializer
    queryset = Occupation.objects.all()


class OccupationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OccupationSerializer
    queryset = Occupation.objects.all()


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
