from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Create your models here.

# DB Model representing the supplier
class Supplier(models.Model):
    # Unique identifier for the supplier
    supplier_id = models.AutoField(max_length=16,
                                   primary_key=True)
    
    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")
    # Supplier Name
    name = models.CharField(max_length=35,
                            blank=False,
                            help_text="Name of the supplier")
    
    # Supplier Address line 1
    address_1=models.CharField(max_length=35,
                               blank=False,
                               help_text="Address line 1")
                               
    # Supplier Address line 2
    address_2=models.CharField(max_length=35,
                               blank=False,
                               help_text="Address line 2")

    # Supplier City
    city=models.CharField(max_length=35,
                          blank=False,
                          help_text="City of the supplier") 

    # Supplier Country
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
    country = models.CharField(max_length=3,
                               choices=COUNTRY_OF_ORIGIN,
                               default=COUNTRY_CHINA,
                               help_text="Represents the supplier country")
                               
    # Post code of the supplier
    post_code=models.CharField(max_length=10,
                               blank=False,
                               help_text="Post code of the supplier") 
                               
    # Phone number of the supplier                               
    phone_number=models.CharField(max_length=10,
                                  blank=False,
                                  help_text="Phone number of the supplier")

    create_dateTime = models.DateTimeField(auto_now_add=True)
   
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")

    # return the supplier name
    def __unicode__(self):  
        return self.name
    
    # reverse url
    def get_absolute_url(self):
        return reverse('supplier-view', kwargs={'pk': self.pk})

 
# DB Model representing the Purchase order Header
class PurchaseOrder(models.Model):
    # Unique identifier for the purchase order
    purchase_order_number = models.AutoField(max_length=16,
                                             primary_key=True)
    
    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")

    # Store identifier
    store_id = models.CharField(max_length=12,
                                blank=False,
                                help_text="Store Identifier")                                       
    
    # Supplier Identifier    
    supplier_id =  models.CharField(max_length=16,
                                    blank=False,
                                    help_text="Supplier Identifier")
    
    # Status of the Purchase Order    
    status_code =  models.CharField(max_length=2,
                                    blank=False,
                                    help_text="Status of the purchase order")
    
    # Expected Arrival Date
    expected_arrival_date = models.DateField(blank=True,
                                             help_text="Expected arrival date of the order item")
    
    #Create date time and user
    create_dateTime = models.DateTimeField(auto_now_add=True)
   
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")
    
                                 
    # return the supplier name
    def __unicode__(self):  
        return self.purchase_order_number
    
    # reverse url
    def get_absolute_url(self):
        return reverse('po-view', kwargs={'pk': self.pk})

# DB Model representing the Purchase order Detail
class PurchaseOrderDtl(models.Model):
    # Unique identifier for the purchase order dtl
    purchase_order_dtl_id = models.AutoField(max_length=16,
                                            primary_key=True)

    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")

    # Unique identifier for the purchase order dtl
    purchase_order_number = models.CharField(max_length=16,
                                             blank=False,
                                             help_text="PO Number")
                                            
    sku_id = models.CharField(max_length=20,
                              blank=False,
                              help_text="Unique identifier of the SKU")
                              
    dsp_sku = models.CharField(max_length=46,
                              blank=False,
                              help_text="Used to display the item for picking, combination of values like <4343434:I30:2004:CHN>")
                              

    ordered_qty = models.IntegerField(default=0,
                                        help_text="Quantity Ordered for the item");
                                        
    
    create_dateTime = models.DateTimeField(auto_now_add=True)
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")
    
                                 
    # return the supplier name
    def __unicode__(self):  
        return self.purchase_order_dtl_id
    
    # reverse url
    def get_absolute_url(self):
        return reverse('podtl-view', kwargs={'pk': self.pk})


# DB Model representing the Inbound shipment Header
class InboundShipment(models.Model):
    # Unique identifier for the inbound shipment number
    inbd_shipment_number = models.AutoField(max_length=16,
                                            primary_key=True)
    
    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")
    
    # Store identifier
    store_id = models.CharField(max_length=12,
                                blank=False,
                                help_text="Store Identifier")
                                
    # Unique identifier for the purchase order number
    purchase_order_number = models.CharField(max_length=16,
                                             help_text="PO Number")                                
    
    # Status of the inbound shipment    
    status_code =  models.CharField(max_length=2,
                                    blank=False,
                                    help_text="Status of the shipment")
    

    #Create date time and user
    create_dateTime = models.DateTimeField(auto_now_add=True)
   
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")
    
                                 
    # return the supplier name
    def __unicode__(self):  
        return self.inbd_shipment_number
    
    # reverse url
    def get_absolute_url(self):
        return reverse('inboundshipment-view', kwargs={'pk': self.pk})

# DB Model representing the Inbound shipment details
class InboundShipmentDtl(models.Model):
    # Unique identifier for the purchase order dtl
    inbd_shipment_number_dtl_id = models.AutoField(max_length=16,
                                                   primary_key=True)

    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")

    # Unique identifier for the purchase order dtl
    inbd_shipment_number = models.CharField(max_length=16,
                                            blank=False,
                                            help_text="Inbound Shipment Number")
                                            
    sku_id = models.CharField(max_length=20,
                              blank=False,
                              help_text="Unique identifier of the SKU")
                              
    dsp_sku = models.CharField(max_length=46,
                              blank=False,
                              help_text="Used to display the item for picking, combination of values like <4343434:I30:2004:CHN>")
                              

    ordered_qty = models.IntegerField(default=0,
                                        help_text="Quantity Ordered for the item");
                                        
    received_qty = models.IntegerField(default=0,
                                       help_text="Quantity received for the item");
                                        
    create_dateTime = models.DateTimeField(auto_now_add=True)
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")
    
                                 
    # return the supplier name
    def __unicode__(self):  
        return self.inbd_shipment_number_dtl_id
    
    # reverse url
    def get_absolute_url(self):
        return reverse('inboundshipmentdtl-view', kwargs={'pk': self.pk})
