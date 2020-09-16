from django.db import models

# Create your models here.

#  Don't forget to install Pillow otherwise won't be able to use ImageField.
#  To do it run pip install Pillow.
# The __str__ method is used just to get the string representation of the object.

#  After doing above we don't need to write the makemigrations command since we have not done any change to the
#  attributes of the product. We have just added a new function to get the string representation of the object.


class Product(models.Model):

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)

    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default = "")
    description = models.CharField(max_length=300)
    ActualPrice = models.IntegerField(default=0)
    discountedprice = models.IntegerField(default=0)
    publishDate = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
         return self.product_name



class Contact(models.Model):

    msg_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=70,default="")
    Email = models.EmailField(max_length=70,default="")
    MobileNumber = models.IntegerField(default=0)
    WhatsappNumber = models.IntegerField(default=0)
    description = models.CharField(max_length=700,default="")

    def __str__(self):
         return self.Name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=100000)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address1 = models.CharField(max_length=400)
    address2 = models.CharField(max_length=400)
    zip_code = models.CharField(max_length=20)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10] + "...."
















