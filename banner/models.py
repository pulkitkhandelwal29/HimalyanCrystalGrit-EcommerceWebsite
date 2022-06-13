from django.db import models

# Create your models here.
class Banner(models.Model):
    banner_name = models.CharField(max_length=50, unique=True)
    banner_image = models.ImageField(upload_to='photos/banners')

    def __str__(self):
        return self.banner_name
