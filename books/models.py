from django.db import models
from django.urls import reverse

class Books(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
