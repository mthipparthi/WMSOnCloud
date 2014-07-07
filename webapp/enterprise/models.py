from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Create your models here.
''' Model to represent the enterprise master
    which defines the organisation/enterprise
    and the base entity the retail supply chain application.
    Enterprise object cannot be created through web portal, only manual
    SQL addition is allowed.
'''

class EnterpriseMaster(models.Model):
    organisation_id = models.CharField(max_length=3,
                                     primary_key=True,
                                     help_text="Organisation Identifier eg: HAT")

    # Name of the organisation
    organisation_name = models.CharField(max_length=70,
                                         blank=False,
                                         help_text="Name of the organisation")

    # Address of the organisation
    address_1 = models.CharField(max_length=35,
                                 blank=False,
                                 help_text="Address Line 1 of the organisation")

    address_2 = models.CharField(max_length=35,
                                 null=True,
                                 help_text="Address Line 2 of the organisation")

    suburb = models.CharField(max_length=20,
                              blank=False,
                              help_text="City/Suburb of the organisation")

    state = models.CharField(max_length=20,
                             blank=False,
                             help_text="State of the organisation")

    country = models.CharField(max_length=20,
                               blank=False,
                               help_text="Country of the organisation")

    # Post Code
    post_code = models.CharField(max_length=20,
                                 blank=False,
                                 help_text="Post Code of the organisation")
    # Phone Number
    phone_nbr = models.CharField(max_length=20,
                                 null=True,
                                 help_text="Contact Phone Number")

    # Fax Number
    fax_nbr = models.CharField(max_length=20,
                               null=True,
                               help_text="Contact Fax Number")

    # Contact Person Details
    contact_person_surname = models.CharField(max_length=35,
                                              blank=True,
                                              help_text="Contact person's surname")

    contact_person_firstname = models.CharField(max_length=35,
                                                blank=True,
                                                help_text="Contact person's first name")

    # Indicator to show the work flows enabled for the organisation
    enable_dc_flow = models.BooleanField(default=True,
                                         help_text="Indicates organisation have distribution flow")

    enable_store_flow = models.BooleanField(default=True,
                                            help_text="Indicates organisation have retail store flow")

    enable_account_flow = models.BooleanField(default=True,
                                              help_text="Indicates organisation have account flow")

    # If organisation is hosted in its own transaction DB, then enter the DB credential
    db_user_name = models.CharField(max_length=35,
                                    null=True,
                                    help_text="Database user name")


    # encrypt the DB before storing it.
    db_pswd = models.CharField(max_length=35,
                               null=True,
                               help_text="Database user name")

    db_schema_name = models.CharField(max_length=35,
                                      null=True,
                                      help_text="Database schema name")


    # parent organisation id
    parent_organisation_id = models.CharField(max_length=3,
                                              null=True,
                                              help_text="Parent organisation name")

    create_dateTime = models.DateTimeField(auto_now_add=True)
    create_user_name = models.CharField(max_length=10,
                                        help_text="User id created the record")

    # return the organisation id
    def __unicode__(self):
        return self.organisation_id

    # reverse url
    def get_absolute_url(self):
        return reverse('item-view', kwargs={'pk': self.pk})
