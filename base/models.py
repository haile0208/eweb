from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(null=True,blank=True,upload_to= "images/")
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("base:product", kwargs={"slug": self.slug})
    

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title