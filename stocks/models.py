from django.db import models
from party.models import party_Ledger
from commodity.models import Commodity
# Create your models here.


class Stocks(models.Model):
    """
    Model representing stock each party host
    """

    def number():
        no = Stocks.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    lot = models.IntegerField(unique=True, default=number)
    date = models.DateField()
    Name = models.ForeignKey(party_Ledger, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    begs = models.IntegerField()
    boxes = models.IntegerField()
    remarks = models.TextField(max_length=200, null=False)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.lot)