from django.db import models


class Place(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=200)

    def __str__(self):
        return self.short_description


class Way(models.Model):
    source = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='outgoing_ways')
    destination = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='incoming_ways')
    description = models.TextField()
    short_description = models.CharField(max_length=200)

    def __str__(self):
        return self.short_description
