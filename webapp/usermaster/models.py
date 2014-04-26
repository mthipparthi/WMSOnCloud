from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

#    Create    your    models    here.
class    UserMasterManager(BaseUserManager):
    def    _create_user(self,email, password,is_staff,is_superuser,**extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,is_staff=is_staff,is_active=True,
                        is_superuser=is_superuser,last_login=now,
                        date_joined=now,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def  create_user(self,email,password=None,**extra_fields):
        return self._create_user(email,password,False,False,**extra_fields)

    def  create_superuser(self,email,password,**extra_fields):
        return self._create_user(email,password,True,True,**extra_fields)

class    UserMaster(AbstractBaseUser):
    """
    Email and password are required.Other fields are optional.

    """
    USER_SALUTATION_MR = 'MR'
    USER_SALUTATION_MRS = 'MRS'
    USER_SALUTATION_MS = 'MS'
    USER_SALUTATION_CHOICES = ((USER_SALUTATION_MR, 'Mr'),
                               (USER_SALUTATION_MRS, 'Mrs'),
                               (USER_SALUTATION_MS, 'Ms'),
                              )

    email = models.EmailField(_('Email Address'), max_length=30, unique=True)
    title = models.CharField(_('Title'), max_length=5, blank=True, choices = USER_SALUTATION_CHOICES,default = USER_SALUTATION_MR)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    enterprise_id = models.CharField(_('Enterprise ID'), max_length=30, blank=False)
    store_id = models.CharField(_('Store ID'), max_length=30, blank=False)
    job_title = models.CharField(_('Job Title'), max_length=30, blank=True)
    date_joined = models.DateField(_('Date Joined'), default=timezone.now)
    date_expiry = models.DateField(_('Expiry Date'), default=timezone.now)

    is_staff = models.BooleanField(_('Staff Status'),    default=False,
        help_text=_('Designates Whether The User can log into this admin site.'))
    is_active = models.BooleanField(_('Active'),    default=True,
        help_text=_('Select to Activate or Unselect To Deactivate'))

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserMasterManager()

    USERNAME_FIELD = 'email'
    #    REQUIRED_FIELDS = ['organization_id','default_store_id']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ["-email"]

    def get_absolute_url(self):
        #return "/usermaster/user/%s/"%urlquote(self.id)
        return reverse('user_detail', kwargs={'pk': self.pk})

    def get_full_name(self):
        full_name = '%s    %s'%(self.first_name,self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def check_password(self,password):
        return self.password == password

    def as_json(self):
        return dict(
            email=self.email,
            title=self.title,
            first_name=self.first_name,
            last_name=self.last_name,
            enterprise_id=self.enterprise_id,
            store_id=self.store_id,
            job_title=self.job_title,
            is_active=self.is_active,
            date_joined=self.date_joined.isoformat(),
            date_expiry=self.date_expiry.isoformat())

