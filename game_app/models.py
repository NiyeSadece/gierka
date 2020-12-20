from django.db import models


class Place(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=200)

    def __str__(self):
        return self.short_description
