from django.db import models


class ShortenedUrls(models.Model):
    url = models.URLField()
