from	django.forms	import	ModelForm
from	django.db	import	models
from	useradmin.models	import	UserMaster
from	django	import	forms
from	django.forms	import	CharField,	Form,	PasswordInput

#	Create	your	models	here.

class	UserVerificationForm(ModelForm):
	"""
	UserVerificationForm
	"""
	#email	=	forms.EmailField(max_length=30)
	#password	=	CharField(widget=PasswordInput())
	#enterprise_id	=	forms.CharField(max_length=30)
	class	Meta:
		model	=	UserMaster
		fields	=	['email',	'password',	'enterprise_id']

class	UserCreationForm(ModelForm):
	"""
	UserCreationForm
	"""
	class	Meta:
		model	=	UserMaster

class	UserUpdateForm(ModelForm):
	"""
	UserCreationForm
	"""
	class	Meta:
		model	=	UserMaster
