from	django	import	forms
from	storemaster.models	import	StoreMaster

class	StoreMasterForm(forms.ModelForm):
	#store_id	=	forms.CharField()
	#store_name	=	forms.CharField(widget=forms.Textarea)
	class	Meta:
		model	=	StoreMaster
		fields	=	['store_id','store_name','oraganisation_id','address_1','address_2','suburb','state','country','post_code','phone_nbr','dsitribution_centre_flag','rcv_without_shipment','locations_exist','local_currency','display_local_currency','create_user_id','create_date_time','receive_with_lpn','putaway_tasks_needed','picking_tasks_enabled','store_order_allocation_enabled','cash_sale_return_period','credit_sale_return_period']	#	list	of	fields	you	want	from	model

