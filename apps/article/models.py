from ckeditor.fields import RichTextField
from django.db import models

from apps.common.models import BaseModel, User


class Occupation(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "occupation"
        verbose_name_plural = "occupations"


class AuthorSocialMedia(BaseModel):
    name = models.CharField(max_length=55)
    icon = models.FileField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=55)
    address = models.TextField()
    social_media = models.ForeignKey(AuthorSocialMedia, related_name="author_social", on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, related_name="author_occupation", on_delete=models.CASCADE)
    picture = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    subscription_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "subscription"


class Instagram(BaseModel):
    picture = models.ImageField()
    url = models.URLField()

    class Meta:
        verbose_name = "InstagramLink"


class Category(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories   "


class Tag(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"


class Article(BaseModel):
    name = models.CharField(max_length=125)
    author = models.ForeignKey(Author, related_name="article", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    tag = models.ManyToManyField(
        Tag,
        related_name="tag",
    )
    description = RichTextField(config_name="awesome_ckeditor")
    read_time = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


class Comment(BaseModel):
    user = models.ManyToManyField(
        User,
        related_name="comment",
    )
    article = models.ForeignKey(Author, related_name="comment", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
