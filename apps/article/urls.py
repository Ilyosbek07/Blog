from django.urls import path

from apps.article.views import (
    ArticleListCreateAPIView,
    ArticleRetrieveUpdateDestroyAPIView, \
    AuthorListCreateAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    TagListCreateAPIView,
    TagRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    OccupationListCreateAPIView,
    OccupationRetrieveUpdateDestroyAPIView,
    SubscriptionListCreateAPIView,
    SubscriptionRetrieveUpdateDestroyAPIView,
    InstagramListCreateAPIView,
    InstagramRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("", ArticleListCreateAPIView.as_view()),
    path("<int:pk>/", ArticleRetrieveUpdateDestroyAPIView.as_view()),

    path("tag/", TagListCreateAPIView.as_view()),
    path("tag/<int:pk>/", TagRetrieveUpdateDestroyAPIView.as_view()),

    path("author/", AuthorListCreateAPIView.as_view()),
    path("author/<int:pk>/", AuthorRetrieveUpdateDestroyAPIView.as_view()),

    path("category/", CategoryListCreateAPIView.as_view()),
    path("category/<int:pk>/", CategoryRetrieveUpdateDestroyAPIView.as_view()),

    path("occupation/", OccupationListCreateAPIView.as_view()),
    path("occupation/<int:pk>/", OccupationRetrieveUpdateDestroyAPIView.as_view()),

    path("subscription/", SubscriptionListCreateAPIView.as_view()),
    path("subscription/<int:pk>/", SubscriptionRetrieveUpdateDestroyAPIView.as_view()),

    path("instagram/", InstagramListCreateAPIView.as_view()),
    path("instagram/<int:pk>/", InstagramRetrieveUpdateDestroyAPIView.as_view()),
]
