from	django.shortcuts	import	render
from	django.http	import	HttpResponseRedirect
from	django.http	import	HttpResponse
from	django.contrib.auth	import	authenticate,	login
from	django.core.context_processors	import	csrf

from	django.views.generic.edit	import	CreateView
from	django.views.generic.edit	import	UpdateView
from	django.views.generic.edit	import	DeleteView
from	django.views.generic.detail	import	DetailView

from	usermaster.models	import	UserMaster
from	usermaster.forms	import	UserVerificationForm
from	usermaster.forms	import	UserCreationForm
from	usermaster.forms	import	UserUpdateForm


#	Create	your	views	here.
def	UserLoginView(request):
	if	request.method	==	'POST':	#	If	the	form	has	been	submitted...
		print(request.POST)
		form	=	UserVerificationForm(request.POST)	#	A	form	bound	to	the	POST	data
		if	form.is_valid():
			email	=	request.POST.get('email',	'')
			password	=	request.POST.get('password',	'')
			enterprise_id	=	request.POST.get('enterprise_id',	'')
			user	=	authenticate(email=email,	password=password)
			if	user.is_active:
				login(request,	user)
				#	Redirect	to	a	success	page.
				return	HttpResponse('Success')
	else:
		form	=	UserVerificationForm()
	return	render(request,	'index.html',	{'form':	form,	})

class	UserCreationView(CreateView):
	model	=	UserMaster
	#	fields	=	['store_id','store_name']
	form_class	=	UserCreationForm
	template_name	=	'usermaster/user_create_form.html'

class	UserUpdateView(UpdateView):
	model	=	UserMaster
	form_class	=	UserUpdateForm
	template_name	=	'usermaster/user_update_form.html'

class	UserDeleteView(DeleteView):
	model	=	UserMaster
	template_name	=	'usermaster/user_delete_form.html'
	success_url	=	'Success'

class	UserDetailView(DetailView):
	model	=	UserMaster
	template_name	=	'usermaster/user_detail_form.html'


