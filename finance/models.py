from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey 
import uuid
from django.db.models.signals import post_save
# Create your models here.

User = get_user_model()
class Wallet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2,max_digits=1000)
    uuid = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)

    def __str__(self):
        return str(self.user)
class WalletAction(models.Model):
    action_values = (('W','Withdraw'),('D','Deposit'),('B','Bid'),('S','Subscription'))
    action = models.CharField(choices=action_values,max_length=2,primary_key=True)
    credit = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.action


class Transaction(models.Model):

    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    uuid = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    wallet_action = models.ForeignKey(WalletAction,on_delete=models.DO_NOTHING,null=True)
    description = models.CharField(max_length=255,default="Bid made to Afraha")

    def __str__(self) -> str:
        return f'{self.wallet} - {self.amount}'

def transaction_wallet_update(sender,instance,**kwargs):
    wallet_action = instance.wallet_action
    wallet=Wallet.objects.get(id=instance.wallet.id)

    if wallet_action.credit:
        wallet.balance = float(wallet.balance)-instance.amount
        wallet.save()
    else:
        wallet.balance = float(wallet.balance)+instance.amount
        wallet.save()

post_save.connect(transaction_wallet_update,sender=Transaction)
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=100)

    def __str__(self) -> str:
        return self.name

class Subscription(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name="service")
    renewal_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.wallet.user} - {self.service}'
