from django.db import models
from django.core.urlresolvers import reverse
import datetime


# Create your models here.
class LocationMaster(models.Model):
    # Location Identifier - Auto generated primary key
    location_id = models.AutoField(max_length=16,
                                   primary_key=True)
    
    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")
    # Store identifier
    store_id = models.CharField(max_length=12,
                                blank=False,
                                help_text="Store Identifier")
    
    # Area of the location
    area = models.CharField(max_length=3,
                            help_text="Area of the location in the store, will be a drop down")
                            
    # Zone of the location
    zone = models.CharField(max_length=3,
                            help_text="Zone of the location in the store")

    # Aisle of the location                        
    aisle = models.CharField(max_length=3,
                             blank=False,
                             help_text="Aisle of the location")
    # Bay of the location
    bay = models.CharField(max_length=3,
                           blank=False,
                           help_text="Bay of the location")
    
    # Level of the location
    level = models.CharField(max_length=3,
                             blank=False,
                             help_text="Level of the location like 1, 2,3")
                             
    # Sequence of the location in an aisle, this will be the same for all the locations 
    # on the same aisle/bay irrespective of the level
    sequence = models.IntegerField(help_text="Sequence of the location to define the work path in an aisle")
    
    # Display location, which is aisle-bay-level
    dsp_location=models.CharField(max_length=12,
                                  blank=False,
                                  help_text="Location displayed to the user as aisle-bay-level")    
     
    #location dimensional data
    
    # Maximum volume of the location - TODO apply a default logic
    max_volume = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=10,
                                    decimal_places=2,
                                    help_text="Maximum volume of the location")
    
    # Current volume - can be null
    current_volume = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    default=0.0,
                                    help_text="Current volume of the location")
                            
    # Maximum weight of the location - TODO apply a default logic                            
    max_weight = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=10,
                                    decimal_places=2,
                                    help_text="Maximum weight of the location")
    
    # Current weight - can be null
    current_weight = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=10,
                                    decimal_places=2,
                                    default=0.0,
                                    help_text="Current weight of the location")

    # Maximum height of the location - TODO apply a default logic                                 
    max_height = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=7,
                                    decimal_places=2,
                                    help_text="Maximum height of the location")

    # Maximum number of the skus that can be assigned to a location
    max_number_of_items = models.IntegerField(help_text="Maximum number of distinct items that can be in the location")                                    
    create_dateTime = models.DateTimeField(auto_now_add=True)
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")
    # return the item name as the item name
    def __unicode__(self):  
        return self.dsp_location
    
    # reverse url
    def get_absolute_url(self):
        return reverse('locn-view', kwargs={'pk': self.pk})
        
    def save(self):
        self.dsp_location = self.aisle
        self.dsp_location += "-"
        self.dsp_location += self.bay
        self.dsp_location += "-"
        self.dsp_location += self.level
        super(LocationMaster, self).save()