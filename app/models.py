from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FoodItem(models.Model):

    name = models.CharField(max_length=100)

    price = models.FloatField()

    category = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(upload_to='foods/')
    image = models.ImageField(
    upload_to='foods/',
    null=True,
    blank=True
)

    def __str__(self):
        return self.name

class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )

    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username