from django.db import models
from accounts.models import Account
from store.models import*

# Create your models here.

class Cart(models.Model):
  cart_id = models.CharField(max_length=250, blank=True)
  date_added = models.DateField(auto_now=True)

  def __str__(self):
    return self.cart_id

class CartItem(models.Model):
  user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  variation = models.ManyToManyField(Variation, blank=True)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
  quantity = models.IntegerField()
  is_active = models.BooleanField(default=True)

  def sub_total(self):
    return self.product.price * self.quantity
  
  def __unicode__(self):
    return self.product
  # The __unicode__() method is called whenever you call unicode() on an object. Since Django's database backends will return Unicode strings in your model's attributes.