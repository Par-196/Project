from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    number = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images')
    image_site = models.ImageField(blank=True, upload_to='images')
    currency = models.CharField(max_length=1)
    grade = models.CharField(max_length=5)
    def __str__(self):
        return self.name

