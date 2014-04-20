from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Create your models here.
class LocationInventory(models.Model):
    # Location Identifier
    location_id = models.CharField(max_length=16,
                                    blank=False,
                                    help_text="Location Identifier")
    
    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")
    # Store identifier
    store_id = models.CharField(max_length=12,
                                blank=False,
                                help_text="Store Identifier")
    
    # Display location, which is aisle-bay-level
    dsp_location=models.CharField(max_length=12,
                                  blank=False,
                                  help_text="Location displayed to the user as aisle-bay-level")

    sku_id = models.CharField(max_length=20,
                              blank=False,
                              help_text="Unique identifier of the SKU")
                              
    dsp_sku = models.CharField(max_length=46,
                              blank=False,
                              help_text="Used to display the item for picking, combination of values like <4343434:I30:2004:CHN>")
                              

    inventory_qty = models.IntegerField(default=0,
                                        help_text="Quantity of the item");
                                        
    
    create_dateTime = models.DateTimeField(auto_now_add=True)
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")
    
    last_sell_datetime = models.DateTimeField();
    # return the item name as the item name
    def __unicode__(self):  
        return self.dsp_sku
    
    # reverse url
    def get_absolute_url(self):
        return reverse('inventory-view', kwargs={'pk': self.pk})
