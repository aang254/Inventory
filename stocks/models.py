from django.db import models
from party.models import party_Ledger
from commodity.models import Commodity
from django.db.models import Max
# Create your models here.


class Stocks(models.Model):
    """
    Model representing stock each party host
    """
    def number():
        no = Stocks.objects.all().aggregate(Max('lot'))
        numb = no['lot__max']
        if numb == None:
            return 1
        else:
            return numb + 1

    lot = models.IntegerField(primary_key=True, default=number)
    date = models.DateField()
    Name = models.ForeignKey(party_Ledger, on_delete=models.PROTECT)
    commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT)
    begs = models.IntegerField(default=0)
    boxes = models.IntegerField(default=0)
    rem_beg = models.IntegerField(default=0)
    rem_box = models.IntegerField(default=0)
    remarks = models.TextField(max_length=200, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.lot) + '*' + str(self.date) + '*' + str(self.Name) + '*' + str(self.commodity) + '*' + \
               str(self.begs) + '*' + str(self.boxes) + '*' + str(self.remarks)

