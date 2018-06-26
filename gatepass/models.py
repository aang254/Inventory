from django.db import models
from stocks.models import Stocks
from party.models import party_Ledger
from commodity.models import Commodity
# Create your models here.

class gate_pass(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    passNo = models.IntegerField(unique=True,blank=False)
    date = models.DateField()
    driver_name = models.CharField(max_length=30,null=True)
    Auto_No = models.CharField(max_length=20,null=True)
    lot = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, null=False)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    Address = models.TextField(max_length=200, null=True)
    gstin = models.CharField('GSTIN', max_length=15, null=False)
    bill_no = models.CharField(max_length=40,null=False)
    bags = models.IntegerField()
    boxes = models.IntegerField()
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Name
