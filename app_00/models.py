from django.db import models

# Create your models here.
class BookShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Booking')
    description = models.TextField(verbose_name='Description')
    rating = models.FloatField(default=0, verbose_name='Rating')
    url = models.URLField(verbose_name='Internet address')

    class Meta:
        verbose_name = 'Book Shop'
        verbose_name_plural = 'Book Shops'

    def __str__(self):
        return self.name


class Book(models.Model):
    bookshoop = models.ForeignKey(BookShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Book title')
    short_description = models.CharField(max_length=30, verbose_name='Book description')
    price = models.IntegerField(default=0, verbose_name='Price')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name']

    def __str__(self):
        return self.name


