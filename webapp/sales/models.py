from django.db import models

# Create your models here.
class SellTransaction(models.Model) :
    # Unique identifier for the Sales Transaction
    invoice_number = models.AutoField(max_length=16,
                                      primary_key=True)
    
    # Organisation name    
    organisation_id = models.CharField(max_length=3,
                                       blank=False,
                                       help_text="Organisation Identifier eg: HAT")
    # Store id                                   
    store_id = models.CharField(max_length=12,
                                help_text="Store Identifier")  
    
    # Customer Identifier
    customer_id = models.CharField(max_length=35,
                                   help_text="Customer Identifier")
                               
    # Payment Type
    payment_type = models.CharField(max_length='6',
                                    default='CASH',
                                    help_text="Payment Type")

    # Payment status
    payment_status = models.CharField(max_length='6',
                                      default='PAID',
                                      help_text="Payment Status")
                                    
    # Transaction type
    transaction_type = models.CharField(max_length='6',
                                       default='SELL',
                                        help_text="Tyep of transaction. sales or refund")

    ref_invoice_number = models.CharField(max_length=16,
                                          help_text="Reference invoice number for the refund")


    total_amount = models.IntegerField(default=0,
                                       help_text="Total Amount")

    tax = models.IntegerField(default=0,
                              help_text="Total Tax")

    invoice_dateTime = models.DateTimeField(auto_now_add=True)
    
    invoice_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")                              

    # return the supplier name
    def __unicode__(self):  
        return self.invoice_number
    
    # reverse url
    def get_absolute_url(self):
        return reverse('sales-view', kwargs={'pk': self.pk})



# Sales Transaction Details
class SellTransactionDtl(models.Model) :
    # Unique identifier for the Sales Transaction dtl
    invoice_dtl_id = models.AutoField(max_length=16,
                                      primary_key=True)
                                      
    invoice_number = models.CharField(max_length=16,
                                      blank=False,
                                      help_text="Invoice number")
                                      
    item_barcode = models.CharField(max_length=20,
                                    blank=False,
                                    help_text="Bar code of the item")

    qty_sold = models.IntegerField(default=0,
                                   help_text="Quantity Sold")

    sell_price = models.IntegerField(default=0,
                                     help_text="Sales Price")
   
    invoice_dateTime = models.DateTimeField(auto_now_add=True)
    
    invoice_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")                             

    # return the item barcode name
    def __unicode__(self):  
        return self.item_barcode
    
    # reverse url
    def get_absolute_url(self):
        return reverse('salesdtl-view', kwargs={'pk': self.pk})
        

