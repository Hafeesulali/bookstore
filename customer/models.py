from django.db import models
from book.models import Books
from django.contrib.auth.models import User


# from django.contrib.auth import models

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=120)
#     last_name = models.CharField(max_length=120)
#     email = models.CharField(max_length=120, unique=True)
#     username = models.CharField(max_length=120, unique=True)
#     password = models.CharField(max_length=120)

class Carts(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    options = (
        ("incart", "incart"),
        ("order placed", "order placed"),
        ("cancelled", "cancelled")
    )
    status = models.CharField(max_length=15, choices=options, default="incart")
