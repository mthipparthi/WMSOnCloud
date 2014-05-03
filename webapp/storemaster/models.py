from django.db import models
from django.core.urlresolvers import reverse
import datetime


# Create your models here.
class StoreMaster(models.Model):
    # Location Identifier - Auto generated primary key
    store_id = models.AutoField(max_length=16, primary_key=True)
    # Organisation name
    store_name = models.CharField(max_length=70,blank=False)
    # Store identifier
    oraganisation_id = models.CharField(max_length=15,blank=False)
    # Area of the location
    address_1 = models.CharField(max_length=20,blank=True)
    # Zone of the location
    address_2 = models.CharField(max_length=20,blank=True)
    # Aisle of the location
    suburb = models.CharField(max_length=20, blank=True)
    # Bay of the location
    state = models.CharField(max_length=20,blank=True)

    country = models.CharField(max_length=20,blank=True)
    # Area of the location
    post_code = models.CharField(max_length=20,blank=True)
    # Zone of the location
    phone_nbr = models.CharField(max_length=20,blank=True)
    # Aisle of the location
    local_currency = models.CharField(max_length=20, blank=True)
    display_local_currency = models.BooleanField(default=True)
    dsitribution_centre_flag = models.BooleanField(default=True)
    rcv_without_shipment = models.BooleanField(default=True)
    locations_exist = models.BooleanField(default=True)
    receive_with_lpn = models.BooleanField(default=True)
    putaway_tasks_needed = models.BooleanField(default=True)
    picking_tasks_enabled = models.BooleanField(default=True)
    store_order_allocation_enabled = models.BooleanField(default=True)
    cash_sale_return_period = models.BooleanField(default=True)
    credit_sale_return_period = models.BooleanField(default=True)
    create_user_id = models.CharField(max_length=20, blank=True)
    create_dateTime = models.DateTimeField(auto_now_add=True)
    create_user_name = models.CharField(max_length=10)
    # return the item name as the item name
    def __unicode__(self):
        return self.store_name

    # reverse url
    def get_absolute_url(self):
        return reverse('store-view', kwargs={'pk': self.pk})
