from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey 
import uuid
# Create your models here.

User = get_user_model()
class Wallet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2,max_digits=1000)
    uuid = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)

    def __str__(self):
        return str(self.user)

class Transaction(models.Model):
    action_values = (('W','Withdraw'),('D','Deposit'))
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    uuid = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    action = models.CharField(choices=action_values,max_length=2)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.wallet} - {self.amount}'

