# Generated by Django 4.1.5 on 2023-01-28 15:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_profile_article_author_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("profile", "0002_rename_profile_author"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Author",
            new_name="Profile",
        ),
    ]
