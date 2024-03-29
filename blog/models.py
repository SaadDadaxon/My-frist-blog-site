from django.db import models
from profile.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=228)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=228)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=228)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles')
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.user.get_full_name():
            return f"{self.author.user.get_full_name()}'s comment"
        return f"{self.author.user.username()}'s comment"

