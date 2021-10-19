from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
USER = get_user_model()
class Farm(models.Model):
    user = models.OneToOneField(USER,on_delete=models.CASCADE,related_name="user_farm_relation")
    farm_name = models.TextField()
    city = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='farmLogos',blank=True,null=True)


    def __str__(self) -> str:
        return self.farm_name

#Location model
class Location(models.Model):
    longitude = models.CharField(max_length=100,blank=True,null=True)
    latitude = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.longitude}-{self.latitude}'


class Branch(Location):
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE,related_name='branch')
    branch_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.farm.farm_name}-{self.branch_name}'

    class Meta:
        verbose_name_plural = "Branches"

class Product(models.Model):
    product_name = models.CharField(max_length=150,blank=False,null=False)
    svg_icon = models.FileField(upload_to="product_svg")
    image = models.ImageField(upload_to="produce=t_image")
    colorCode = models.CharField(max_length=10)


    def __str__(self) -> str:
        return self.product_name


class Produce(models.Model):
    '''
    Produce made by farmer
    name: Unique name to identify produce(optional),
    least_orderable: Least amount to order

    '''

    name = models.TextField(blank=True,null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE,related_name="produce_farm")
    product = models.ForeignKey(Product, on_delete=models.PROTECT,related_name="produce_product")
    weight_kgs = models.IntegerField()
    starting_price = models.DecimalField(decimal_places=2,max_digits=16)
    least_orderable = models.IntegerField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self) -> str:
        return f'{self.farm.farm_name}-{self.name}'
class ProduceImages(models.Model):
    produce = models.ForeignKey(Produce,on_delete=models.CASCADE,related_name='produce_images',blank=True,null=True)

    image = models.ImageField(upload_to="produce_images",null=True)

    

    class Meta:
        verbose_name_plural = 'Produce Images'


    def __str__(self): 
        return f'{self.produce} - {self.image}'



class Bid(models.Model):
    status_values = (('A','Accepted'),('P','Pending'),('R','Rejected'))
    user = models.ForeignKey(USER, on_delete=models.CASCADE,related_name='bid_user')
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE,related_name="bid_produce")
    kilograms = models.IntegerField()
    bid_price = models.DecimalField(decimal_places=2,max_digits=16)

    status = models.CharField(choices=status_values,default="P",max_length=1)
    date_made = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.kilograms * self.bidPrice

    def format_date(self):
        return self.timestamp.strftime('%B')

    def __str__(self):
        return f'{self.user} - {self.produce.farm} - {self.bid_price}'







    