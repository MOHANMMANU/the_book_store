from django.db import models
from django.urls import reverse
class Book(models.Model):
    def get_absolute_url(self):
        return reverse('books:detail',kwargs={'pk': self.pk})


    def __str__(self):
        return self.name+"-"+ self.auther
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)