from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products_images/', default='blank.webp',  null=True, blank=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name
