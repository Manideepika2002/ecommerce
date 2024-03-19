from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
import datetime
from django.dispatch import receiver


class ProfileModel(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null= True)
    designation = models.CharField(max_length=100, null= True)
    mobile_number = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(null=True, upload_to='images/' )
    profile_summary = models.TextField(max_length=300, null= True)
    city = models.CharField(max_length=100, null= True)
    state = models.CharField(max_length=100, null= True)
    country = models.CharField(max_length=100, null= True)
    username=models.CharField(max_length=40,null=True)
    password=models.CharField(max_length=10,null=True)
    def str(self):
        return self.save()

class FormalModel(models.Model):
    image=models.ImageField(upload_to='formals/')
    title=models.CharField(max_length=100)
    prize=models.IntegerField()
    description=models.CharField(max_length=10000)
    def str(self):
        return self.title
        

class TshirtsModel(models.Model):
    image=models.ImageField(upload_to='tshirts/')
    title=models.CharField(max_length=100)
    prize=models.IntegerField()
    description=models.CharField(max_length=10000)

    
    def str(self):
        return self.title

class SuitsModel(models.Model):
    image=models.ImageField(upload_to='suits/')
    title=models.CharField(max_length=100)
    prize=models.IntegerField()
    description=models.CharField(max_length=10000)

    def str(self):
        return self.title

class KurtasModel(models.Model):
    image=models.ImageField(upload_to='kurtas/')
    title=models.CharField(max_length=100)
    prize=models.IntegerField()
    description=models.CharField(max_length=10000)

    def str(self):
        return self.title

class TopsModel(models.Model):
    image=models.ImageField(upload_to='tops/')
    title=models.CharField(max_length=100)
    prize=models.IntegerField()
    description=models.CharField(max_length=10000)

    def str(self):
        return self.title

class Product(models.Model):
    product1 = models.ForeignKey(FormalModel, on_delete=models.CASCADE,null=True)
    product2 = models.ForeignKey(TshirtsModel, on_delete=models.CASCADE,null=True)
    product3 =models.ForeignKey(SuitsModel,on_delete=models.CASCADE,null=True)
    product4 =models.ForeignKey(KurtasModel,on_delete=models.CASCADE,null=True)
    product5 =models.ForeignKey(TopsModel,on_delete=models.CASCADE,null=True)
    class Meta:
        pass   
    
    def __str__(self):
        return self.save()


# class CartItem(models.Model):
#     product = models.ForeignKey(FormalModel, on_delete=models.CASCADE,null=True)
#     quantity = models.PositiveIntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True,null=True)
 
#     def __str__(self):
#         return f'{self.quantity} x {self.product.name}'

 



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    total_prize=models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username)+" "+str(self.total_prize) 

class CartItem(models.Model):
    # product1 = models.ForeignKey(FormalModel, on_delete=models.CASCADE,null=True)
    # product2 = models.ForeignKey(TshirtsModel, on_delete=models.CASCADE,null=True)
    # product3 =models.ForeignKey(SuitsModel,on_delete=models.CASCADE,null=True)
    # product4 =models.ForeignKey(KurtasModel,on_delete=models.CASCADE,null=True)
    # product5 =models.ForeignKey(TopsModel,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(FormalModel, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    # user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    user=models.ForeignKey(ProfileModel,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    price=models.FloatField(default=0)
    total_items=models.IntegerField(default=0)
 
    def __str__(self):
        return str(self.user.username)+" "+str(self.product.title)

# @receiver(post_save, sender=CartItem)
# def correct_price(sender, **kwargs):
#     cart_items=kwargs['instance']
#     prize_of_product = product.objects.get(id=cart_items.product.id)
#     cart_items.price=cart_items.quantity * float(price_of_product.prize)
#     total_cart_items=CartItem.objects.filter(user=cart_items.user)
#     Cart=Cart.objects.get(id=cart_items.cart.id)
#     cart.total_prize=cart_items.prize
#     cart.save()

