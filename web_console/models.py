from django.db import models
#from smartfields import fields
#from smartfields.dependencies import FileDependency
#from smartfields.processors import ImageProcessor
# from sorl.thumbnail import ImageField, get_thumbnail
# Create your models here.
 
class ProductLines(models.Model):
    productLine = models.CharField(primary_key= True, max_length= 50)
    description = models.TextField()

    def __str__(self):
        return self.productLine

class Products(models.Model):
    productCode = models.IntegerField(primary_key= True)
    productName = models.CharField(max_length=50)
    product = models.ForeignKey(ProductLines, on_delete= models.CASCADE, related_name= 'Line' )
    instock = models.IntegerField()
    sold = models.IntegerField()
    sale = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    #image = fields.ImageField(upload_to='pictures', dependencies=[
    #    FileDependency(attname='image_jpeg', processor=ImageProcessor(
    #        format='JPEG', scale={'max_width': 600, 'max_height': 600})),
    #])
    #image_jpeg = fields.ImageField(upload_to='pictures', default= "")
    # this method uploads the img, resize it and keep both the root and the resized image    
    
    image = models.ImageField(upload_to = 'pictures/', default = None)
    # simply upload to media/pictures/, nothing change

    # image = ImageField(upload_to= 'pictures/')
    # def save(self, *args, **kwargs):
    #    if self.image:
    #        self.image = get_thumbnail(self.image, '600x600', quality=99, format='JPEG')
    #    super(Products, self).save(*args, **kwargs)
    # this method has good logic but don't know why there is an error

    images = models.CharField(max_length=150, default='')


    def __str__(self):
        return self.productName

class Customer(models.Model):
    userID = models.AutoField(primary_key = True)
    name = models.TextField()
    phoneNumber = models.IntegerField()
    numberOfPurchase = models.IntegerField()
    sale = models.IntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    cart = models.ForeignKey(Products , on_delete= models.CASCADE, related_name= 'cartCode',primary_key = True,unique = True)
    quantity = models.IntegerField()
    totalPrice = models.IntegerField()

    def __str__(self):
        return self.totalPrice

class Order(models.Model):
    orderId = models.AutoField(primary_key = True)
    orders = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name= 'orderCode',default = None)
    order = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name= 'orderId')
    orderedDate = models.DateField()
    shippedDate = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.orderedDate

class Feedback(models.Model):
    feedback = models.ForeignKey(Products, on_delete= models.CASCADE, related_name='feedbackCode')
    feedback = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name='feedbackId')
    Content = models.TextField()
    feedbackDate = models.DateTimeField()

    def __str__(self):
        return self.feedbackDate    
