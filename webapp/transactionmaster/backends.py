from	django.contrib.auth.models	import	User

class	EmailAuthBackend(object):
	"""
	Email	Authentication	Backend
	Allows	a	user	to	sign	in	using	an	email/password	pair	rather	than
	a	username/password	pair.
	"""

	def	authenticate(self,	username=None,	password=None):
		"""	Authenticate	a	user	based	on	email	address	as	the	user	name.	"""
		"""	user	name	is	nothing	but	email	id,to	be	in	sync	with	user	auth	"""
		"""	customization	we	retained	this	way	"""
		try:
			user	=	User.objects.get(email=username)
			if	user.check_password(password)	and	user.is_active:
				return	user
		except	User.DoesNotExist:
			return	None

	def	get_user(self,	user_id):
		"""	Get	a	User	object	from	the	user_id.	"""
		"""	signature	is	kept	as	user_id	but	we	have	to	pass	email	id	as	an	input"""
		"""	this	designed	this	way	to	be	in	sync	with	user	auth	customization	"""
		try:
			return	User.objects.get(pk=user_id)
		except	User.DoesNotExist:
			return	None
