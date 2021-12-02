from django.db import models
from django.urls import reverse


class ChristmasLetter(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    signature = models.CharField(max_length=50)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter-detail', args=[str(self.id)])
