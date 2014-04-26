#	Create	your	views	here.
from	django.shortcuts	import	render
from	django.contrib	import	auth
from	django.http	import	HttpResponseRedirect,HttpResponse
from	django.views.generic.edit	import	CreateView
from	django.views.generic.edit	import	UpdateView
from	django.views.generic.edit	import	DeleteView
from	django.views.generic.detail	import	DetailView
from	storemaster.models	import	StoreMaster
from	storemaster.forms	import	StoreMasterForm


#	Create	your	views	here.
def	index(request):
	#	Redirect	to	a	success	page.
	return	render(request,	'storemaster/index.html');

class	StoreMasterDetailView(DetailView):
	model	=	StoreMaster
	template_name	=	'storemaster/storemaster_details.html'
	def	get_context_data(self,	**kwargs):
		context	=	super(StoreMasterDetailView,	self).get_context_data(**kwargs)
		return	context

class	StoreMasterCreate(CreateView):
	model	=	StoreMaster
	form_class	=	StoreMasterForm
	template_name	=	'storemaster/storemaster_create_form.html'

class	StoreMasterUpdate(UpdateView):
	model	=	StoreMaster
	form_class	=	StoreMasterForm
	template_name	=	'storemaster/storemaster_update_form.html'

class	StoreMasterDelete(DeleteView):
	model	=	StoreMaster
	template_name	=	'storemaster/storemaster_delete_form.html'
	success_url	=	'Success'

