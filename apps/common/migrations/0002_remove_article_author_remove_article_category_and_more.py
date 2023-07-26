# Generated by Django 4.2.3 on 2023-07-25 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='author',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='author',
            name='social_media',
        ),
        migrations.DeleteModel(
            name='InstagramLink',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='author',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='AuthorSocialMedia',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Occupation',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]