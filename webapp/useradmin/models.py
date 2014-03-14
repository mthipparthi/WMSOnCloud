from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserMasterManager(BaseUserManager):

    def _create_user(self, username, password,
                     is_staff, is_superuser):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
            user = self.model(username=username,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None):
        return self._create_user(email, password, False, False)

    def create_superuser(self, username, password):
        return self._create_user(email, password, True, True)

class UserMaster(AbstractBaseUser):
	"""
	A fully featured User model with admin-compliant permissions that uses
	a full-length email field as the username.
	Email and password are required. Other fields are optional.
	"""
	
	email = models.EmailField(_('email address'), max_length=254, unique=True)
	title = models.CharField(_('title'), max_length=5, blank=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	organization_id = models.CharField(_('organization id'), max_length=30, blank=False)
	default_store_id = models.CharField(_('default store id'), max_length=30, blank=False)
	job_title =  models.CharField(_('job title'), max_length=30, blank=True)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	date_expiry = models.DateTimeField(_('expiry date'))
	
	is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
	is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
   
	objects = UserMasterManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['organization_id','default_store_id']
	
	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_absolute_url(self):
		return "/users/%s/" % urlquote(self.email)

	def get_full_name(self):
		"""
		Returns the first_name plus the last_name, with a space in between.
		"""
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		"Returns the short name for the user."
		return self.first_name

	def email_user(self, subject, message, from_email=None):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email])
		
class TransactionMasterManager(models.Manager):

	def create_transaction_group(self, transaction_group_name, store_id):
		pass
		
class TransactionMaster(models.Model):
	"""
	A group master to assign to capture different group to categorize
	under different groups so that transactions can be grouped under them.
	"""
	
	"""
	Transaction Types
	"""
	TRANSACTION_TYPE_TRANSACTION = 'T'
	TRANSACTION_TYPE_ACTION = 'A'
	TRANSACTION_TYPE_CHOICES = (
		(TRANSACTION_TYPE_TRANSACTION,'Transaction'),
		(TRANSACTION_TYPE_ACTION,'Action'),
	)
	
	"""
	Transaction Categories
	"""
	TRANSACTION_CATEGORY_SALES = 'TCSAL'
	TRANSACTION_CATEGORY_STORE_ORDER_MGMT = 'TCSTO'
	TRANSACTION_CATEGORY_INVN_MGMT = 'TCINV'
	TRANSACTION_CATEGORY_ACCOUNTS = 'TCSACC'
	TRANSACTION_CATEGORY_REPORTS = 'TCSREP'
	TRANSACTION_CATEGORY_ADMIN = 'TCSADM'
	TRANSACTION_CATEGORY_CHOICES = (
		(TRANSACTION_CATEGORY_SALES,'Sales'),
		(TRANSACTION_CATEGORY_STORE_ORDER_MGMT,'Store Order Management'),
		(TRANSACTION_CATEGORY_INVN_MGMT,'Inventory Management'),
		(TRANSACTION_CATEGORY_ACCOUNTS,'Accounts'),
		(TRANSACTION_CATEGORY_REPORTS,'Reports'),
		(TRANSACTION_CATEGORY_ADMIN,'Administration'),
	)
	
	"""
	Transaction Sub Categories
	"""
	TRANSACTION_SUB_CATEGORY_CASH_SALES = 'TCSALCSH'
	TRANSACTION_SUB_CATEGORY_CREDIT_SALES = 'TCSALCRD'
	TRANSACTION_SUB_CATEGORY_CHOICES = (
		(TRANSACTION_SUB_CATEGORY_CASH_SALES,'Cash Sales'),
		(TRANSACTION_SUB_CATEGORY_CREDIT_SALES,'Credit Sales'),
	)
	
	
	transaction_id = models.AutoField(_('transaction  id'),primary_key=True)
	transaction_name = models.CharField(_('transaction  name'), max_length=50)
	transaction_friendly_name = models.CharField(_('transaction  name'), max_length=70)
	transaction_type = models.CharField(_('transaction  type'), max_length=1,choices=TRANSACTION_TYPE_CHOICES,default=TRANSACTION_TYPE_TRANSACTION)
	parent_transaction_id = models.PositiveSmallIntegerField(_('parent transaction  id'))
	transaction_category = models.CharField(_('transaction  category'), max_length=5,choices=TRANSACTION_CATEGORY_CHOICES)
	transaction_sub_category = models.CharField(_('transaction sub category'), max_length=8, blank=True,choices=TRANSACTION_SUB_CATEGORY_CHOICES)
	tranaction_config = models.CharField(_('url action'), max_length=100, blank=False)
	create_date_time = models.DateTimeField(_('create date time'))
	mod_date_time = models.DateTimeField(_('modified date time'))
  
	objects = TransactionMasterManager()

	def get_absolute_url(self):
		return "/transactions/%s/" % urlquote(self.transaction_id)

class RoleMasterManager(models.Manager):

	def create_transaction_group(self, transaction_group_name, store_id):
		pass
		
class RoleMaster(models.Model):
	"""
	A group master to assign to capture different group to categorize
	under different groups so that transactions can be grouped under them.
	"""
	role_id = models.AutoField(_('role  id'),primary_key=True)
	role_name = models.CharField(_('role  name'), max_length=50)
	role_friendly_name = models.CharField(_('role friendly name'), max_length=50)
	organization_id = models.CharField(_('organization id'), max_length=30, blank=False)
	create_date_time = models.DateTimeField(_('create date time'))
	mod_date_time = models.DateTimeField(_('modified date time'))
	
	objects = RoleMasterManager()

	def get_absolute_url(self):
		return "/roles/%s/" % urlquote(self.role_id)
		
		

class RoleTransactionMapManager(models.Manager):

	def create_transaction_group(self, transaction_group_name, store_id):
		pass
		
class RoleTransactionMap(models.Model):
	"""
	A group master to assign to capture different group to categorize
	under different groups so that transactions can be grouped under them.
	"""
	TRANSACTION_ENABLED_STATUS_YES = True
	TRANSACTION_ENABLED_STATUS_NO = False
	
	TRANSACTION_ENABLED_STATUS_CHOICES = (
		(TRANSACTION_ENABLED_STATUS_YES,'Yes'),
		(TRANSACTION_ENABLED_STATUS_NO,'No'),
	)
	
	organization_id = models.CharField(_('organization id'), max_length=30, blank=False,db_index=True)
	role_id = models.PositiveSmallIntegerField(_('role  id'), blank=False,db_index=True)
	transaction_id = models.PositiveSmallIntegerField(_('transaction  id'),blank=False)
	transaction_enabled_status = models.BooleanField(_('enabled?'),choices=TRANSACTION_ENABLED_STATUS_CHOICES,default=TRANSACTION_ENABLED_STATUS_NO)
	create_date_time = models.DateTimeField(_('create date time'))
	mod_date_time = models.DateTimeField(_('modified date time'))
			
	objects = RoleTransactionMapManager()

	def get_absolute_url(self):
		return "/roletransactionmaps/%s/" % urlquote(self.role_id)

class UserRoleMapManager(models.Manager):

	def create_transaction_group(self, transaction_group_name, store_id):
		pass
		
class UserRoleMap(models.Model):
	"""
	A group master to assign to capture different group to categorize
	under different groups so that transactions can be grouped under them.
	"""
	
	organization_id = models.CharField(_('organization id'), max_length=30, blank=False,db_index=True)
	user_id = models.PositiveIntegerField(_('user  id'),db_index=True)
	role_id = models.PositiveSmallIntegerField(_('role  id'), blank=False)
	create_date_time = models.DateTimeField(_('create date time'))
	mod_date_time = models.DateTimeField(_('modified date time'))
			
	objects = UserRoleMapManager()

	def get_absolute_url(self):
		return "/userrolemaps/%s/" % urlquote(self.user_id)
		

class UserAccessControlManager(models.Manager):

	def create_transaction_group(self, transaction_group_name, store_id):
		pass
		
class UserAccessControl(models.Model):
	"""
	A group master to assign to capture different group to categorize
	under different groups so that transactions can be grouped under them.
	"""
	USER_ACCESS_KEY_STORE = 'STR'
	USER_ACCESS_KEY_ORGANIZATION = 'ORG'
	USER_ACCESS_KEY_COUNTRY = 'CRY'
	USER_ACCESS_KEY_CHOICES = (
		(USER_ACCESS_KEY_STORE,'Store'),
		(USER_ACCESS_KEY_ORGANIZATION,'Organization'),
		(USER_ACCESS_KEY_COUNTRY,'Country'),
	)
	
	user_id = models.PositiveIntegerField(_('user  id'),db_index=True)
	role_id = models.PositiveIntegerField(_('role  id'),db_index=True)
	role_name = models.CharField(_('role  name'), max_length=50)
	user_access_key = models.CharField(_('user access key'), max_length=3,choices=USER_ACCESS_KEY_CHOICES,default=USER_ACCESS_KEY_STORE)
	user_access_value = models.CharField(_('user access value'), max_length=20)
	create_date_time = models.DateTimeField(_('create date time'))
	mod_date_time = models.DateTimeField(_('modified date time'))
	
	objects = UserAccessControlManager()

	def get_absolute_url(self):
		return "/useracesscontrols/%s/" % urlquote(self.user_id)