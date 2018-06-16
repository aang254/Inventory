from django.db import models
import uuid
# Create your models here.

class party_Ledger(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular Party")
    Name = models.CharField(max_length=200, null=False)
    Address = models.TextField(max_length=200, null=True)
    gstin = models.CharField('GSTIN',max_length=15, null=False,unique=True)
    Contact = models.IntegerField(null=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Name
