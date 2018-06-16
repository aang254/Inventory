from django.db import models

class Commodity(models.Model):
    """
    Model representing a Commodity (e.g. Kismis, makhana,etc).
    """
    name = models.CharField(max_length=200, help_text="Enter a commodity")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
