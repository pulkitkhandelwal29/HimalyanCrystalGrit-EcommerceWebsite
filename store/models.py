from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    images = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class ProductGallery(models.Model):
    product = models.ForeignKey(Product,default =None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products',max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'product gallery'
        verbose_name_plural = 'product gallery'
