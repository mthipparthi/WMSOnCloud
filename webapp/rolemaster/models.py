from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

#Create your models here.

class RoleMasterManager(models.Manager):
    def create_transaction_group(self, transaction_group_name, store_id):
        pass

class RoleMaster(models.Model):
    """
    A group master to assign to capture different group to categorize
    under different groups so that transactions can be grouped under them.
    """
    role_id = models.AutoField(_('Role ID'), primary_key=True)
    role_name = models.CharField(_('Role Name'), max_length=30, blank=False)
    role_friendly_name = models.CharField(_('Role Friendly Name'), max_length=50, blank=True)
    enterprise_id = models.CharField(_('Organization ID'), max_length=30, blank=False)
    create_date_time = models.DateTimeField(_('Create Date Time'))
    mod_date_time = models.DateTimeField(_('Modified Date Time'))

    objects = RoleMasterManager()

    def get_absolute_url(self):
        return  "/roles/%s/"%urlquote(self.role_id)

