from django.db import models
from django.contrib.auth.models import User


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     title = models.CharField(max_length=150, db_index=True)
#     description = models.TextField(null=False,blank=True,db_index=True)
#     RATING_CHOICES=[
#         ("1", "1/5"),
#         ("2", "2/5"),
#         ("3", "3/5"),
#         ("4", "4/5"),
#         ("5", "5/5"),
#     ]
#     rating = models.CharField(max_length=5, choices=RATING_CHOICES,default="5")



class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

class Tag(models.Model):
    name = models.CharField(max_length=1000, db_index=True)



class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True, db_index=True)
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    freeDelivery = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)
    category = models.ForeignKey(Category,default='', null=False,blank=True, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,null=True,blank=True, on_delete=models.CASCADE)

class ProductImage(models.Model):
    product = models.ForeignKey(Product,null=True,blank=True, on_delete=models.CASCADE)
    src = models.ImageField(default=0,upload_to='images')
    alt = models.CharField(max_length=100, default='')

 # class Order(models.Model):
 #    created_at = models.DateTimeField(auto_now_add=True)
 #    fullName = models.CharField(max_length=100, default='', blank=True)
 #    email = models.EmailField(default='',blank=True)

