from django.db import models
#import uuid
from django.core.validators import RegexValidator
# Create your models here.

class party_Ledger(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular Party")
    id = models.IntegerField(primary_key=True,blank=False)
    Name = models.CharField(max_length=200, null=False, unique=True)
    Address = models.TextField(max_length=200, null=True)
    gstin = models.CharField('GSTIN',max_length=15, null=False,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Contact = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id) + '*' + self.Name + '*' +self.Address + '*' + self.gstin + '*' + str(self.Contact)
