from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Create your models here.
class ItemMaster(models.Model):
    sku_id = models.AutoField(max_length=20,
                              primary_key=True)
    organisation_id = models.CharField(max_length=3,
                                       help_text="Organisation Identifier eg: HAT")
    # Name of the item, which is the unique part number for auto mobile spare parts
    # TODO - DB index need to be defined
    item_name = models.CharField(max_length=20,
                                blank=False,
                                help_text="Name of the item, like part number")
    # Unique barcode of the item
    # TODO - DB index need to be defined
    item_barcode = models.CharField(max_length=20,
                                   unique=True,
                                   help_text="Bar code of the item")
    item_description = models.CharField(max_length=70,
                                        help_text="Description of the item like <HeadLight of i30>")
    style = models.CharField(max_length=10,
                             help_text="Style of the item like model of the car")
    size = models.CharField(max_length=10,
                            help_text="Represents the specific feature of the item like year of making")
    # country of origin is defined as a drop down list, currently only very limited countries
    # possibly need to include all the ISO 3 letter codes here.
    COUNTRY_CHINA = 'CHN'
    COUNTRY_SKOREA = 'KOR'
    COUNTRY_INDIA = 'IND'
    COUNTRY_UAE = 'ARE'
    COUNTRY_TAIWAN = 'TWN'
    COUNTRY_GENUINE = 'GEN' # country code used to mark the genuine products
    COUNTRY_OF_ORIGIN = (
        (COUNTRY_CHINA, 'China'),
        (COUNTRY_SKOREA, 'South Korea'),
        (COUNTRY_INDIA, 'India'),
        (COUNTRY_UAE, 'United Arab Emirates'),
        (COUNTRY_TAIWAN, 'Taiwan'),
        (COUNTRY_GENUINE, 'Genuine'),
    )
    country_of_origin = models.CharField(max_length=3,
                                         choices=COUNTRY_OF_ORIGIN,
                                         default=COUNTRY_CHINA,
                                         help_text="Represents the manufacturing country 3 letter ISO code <CHN>")
    # Display sku is defined as a combination of values like item number, model, year and country of origin
    # need to enhance this logic to define the mask at organisation level and also define the separator
    # TODO - DB index need to be defined
    dsp_sku = models.CharField(max_length=46,
                              blank=False,
                              help_text="Used to display the item for picking, combination of values like <4343434:I30:2004:CHN>")
    # This is the buying price excluding the cost of cargo + shipping
    # Not visible to the sales team
    unit_price = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=6,
                                    decimal_places=2,
                                    help_text="Buying price like <10.00>")
    # This is the retail price of the item
    retail_price = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=6,
                                    decimal_places=2,
                                    help_text="Retail selling price like <10.00>")
    # This is the wholesale sale price of the item
    wholesale_price = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=6,
                                    decimal_places=2,
                                    help_text="Wholesale selling price like <10.00>")
    # This is the cost involved for the cargo + handling charges + customs duty
    # Not visible to the sales team
    declaration_cost = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=6,
                                    decimal_places=2,
                                    help_text="Cargo/shipping cost specified in %")                                    
    unit_weight = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=6,
                                    decimal_places=2,
                                    help_text="Weight of the individual item entered in kilograms <0.100>")
    unit_height = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=6,
                                    decimal_places=2,
                                    help_text="Height of the individual item entered in meters <0.100>")                                     
    unit_volume = models.DecimalField(null=False,
                                    blank=False,
                                    max_digits=6,
                                    decimal_places=2,
                                    help_text="Volume of individual item entered in cubic meters <0.100>")
    # Item category needs to be defined as a drop down list, need to come up with the
    # list of categories (mainly for auto mobile retail store now)
    item_category = models.CharField(max_length=10,
                                     help_text="Category like perishable etc")
    create_dateTime = models.DateTimeField(auto_now_add=True)
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")
    # return the item name as the item name
    def __unicode__(self):  
        return self.item_name
    
    # reverse url
    def get_absolute_url(self):
        return reverse('item-view', kwargs={'pk': self.pk})
        
    def save(self):
        self.dsp_sku = self.item_name
        self.dsp_sku += ":"
        self.dsp_sku += self.style
        self.dsp_sku += ":"
        self.dsp_sku += self.size
        self.dsp_sku += ":"
        self.dsp_sku += self.country_of_origin
        super(ItemMaster, self).save()
    
    

