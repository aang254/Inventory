from django.db import models
from stocks.models import Stocks
from party.models import party_Ledger
from commodity.models import Commodity
# Create your models here.

class gate_pass(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    passNo = models.IntegerField(blank=False)
    date = models.DateField()
    driver_name = models.CharField(max_length=30,null=True)
    Auto_No = models.CharField(max_length=20,null=True)
    lot = models.IntegerField()
    Name = models.CharField(max_length=200, null=False)
    commodity = models.CharField(max_length=200, help_text="Enter a commodity")
    gstin = models.CharField('GSTIN', max_length=15, null=False)
    bill_no = models.CharField(max_length=40,null=False)
    bags = models.IntegerField()
    boxes = models.IntegerField()
    def __str__(self):
        """
        String for representing the Model object.
        """

        return str(self.passNo) + "," + str(self.lot) + "," + str(self.date) + "," + str(self.Name)\
               + "," + str(self.commodity) + "," + str(self.bags) + "," + str(self.boxes) + "," + str(self.Auto_No)\
               + "," + str(self.driver_name) + "," + str(self.bill_no) + "," + str(self.gstin)
