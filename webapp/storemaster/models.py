from	django.db	import	models
from	datetime	import	datetime
from	django.core.urlresolvers	import	reverse

#	Create	your	models	here.
class	StoreMaster(models.Model):
	store_id	=	models.CharField(max_length=12)
	store_name	=	models.CharField(max_length=70)
	oraganisation_id	=	models.CharField(max_length=3)
	address_1	=	models.CharField(max_length=35)
	address_2	=	models.CharField(max_length=35)
	suburb	=	models.CharField(max_length=35)
	state	=	models.CharField(max_length=35)
	country	=	models.CharField(max_length=10)
	post_code	=	models.CharField(max_length=10)
	phone_nbr	=	models.CharField(max_length=20)
	dsitribution_centre_flag	=	models.BooleanField(default=True)
	rcv_without_shipment	=	models.BooleanField(default=True)
	locations_exist	=	models.BooleanField(default=True)
	local_currency	=	models.CharField(max_length=3)
	display_local_currency	=	models.BooleanField(default=True)
	create_user_id	=	models.CharField(max_length=10)
	create_date_time	=	models.DateTimeField(default=datetime.now,	blank=True)
	receive_with_lpn	=	models.BooleanField(default=True)
	putaway_tasks_needed	=	models.BooleanField(default=True)
	picking_tasks_enabled	=	models.BooleanField(default=True)
	store_order_allocation_enabled	=	models.BooleanField(default=True)
	cash_sale_return_period	=	models.BooleanField(default=True)
	credit_sale_return_period	=	models.BooleanField(default=True)

	def	get_absolute_url(self):
		return	reverse('storemaster-detail',	kwargs={'pk':	self.pk})
