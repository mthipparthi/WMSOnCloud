from    django.db    import    models
from    django.utils    import    timezone
from    django.utils.http    import    urlquote
from    django.utils.translation    import    ugettext_lazy    as    _
from    django.core.mail    import    send_mail
from    django.contrib.auth.models    import    AbstractBaseUser
from    django.contrib.auth.models    import    BaseUserManager

#    Create    your    models    here.

class    TransactionMasterManager(models.Manager):

        def    create_transaction_group(self,    transaction_group_name,    store_id):
            pass

class    TransactionMaster(models.Model):
    """
    A    group    master    to    assign    to    capture    different    group    to    categorize
    under    different    groups    so    that    transactions    can    be    grouped    under    them.
    """

    """
    Transaction    Types
    """
    TRANSACTION_TYPE_TRANSACTION    =    'T'
    TRANSACTION_TYPE_ACTION    =    'A'

    TRANSACTION_TYPE_CHOICES    =    (
    (TRANSACTION_TYPE_TRANSACTION,    'Transaction'),
    (TRANSACTION_TYPE_ACTION,    'Action'),
    )

    """
    Transaction    Categories
    """
    TRANSACTION_CATEGORY_SALES    =    'TCSAL'
    TRANSACTION_CATEGORY_STORE_ORDER_MGMT    =    'TCSTO'
    TRANSACTION_CATEGORY_INVN_MGMT    =    'TCINV'
    TRANSACTION_CATEGORY_ACCOUNTS    =    'TCSACC'
    TRANSACTION_CATEGORY_REPORTS    =    'TCSREP'
    TRANSACTION_CATEGORY_ADMIN    =    'TCSADM'
    TRANSACTION_CATEGORY_CHOICES    =    (
    (TRANSACTION_CATEGORY_SALES,    'Sales'),
    (TRANSACTION_CATEGORY_STORE_ORDER_MGMT,    'Store    Order    Management'),
    (TRANSACTION_CATEGORY_INVN_MGMT,    'Inventory    Management'),
    (TRANSACTION_CATEGORY_ACCOUNTS,    'Accounts'),
    (TRANSACTION_CATEGORY_REPORTS,    'Reports'),
    (TRANSACTION_CATEGORY_ADMIN,    'Administration'),
    )

    """
    Transaction    Sub    Categories
    """
    TRANSACTION_SUB_CATEGORY_CASH_SALES    =    'TCSALCSH'
    TRANSACTION_SUB_CATEGORY_CREDIT_SALES    =    'TCSALCRD'
    TRANSACTION_SUB_CATEGORY_CHOICES    =    (
                                            (TRANSACTION_SUB_CATEGORY_CASH_SALES,    'Cash    Sales'),
                                            (TRANSACTION_SUB_CATEGORY_CREDIT_SALES,    'Credit    Sales'),
                                            )


    transaction_id    =    models.AutoField(_('transaction    id'),    primary_key=True)
    transaction_name    =    models.CharField(_('transaction    name'),    max_length=50)
    transaction_friendly_name    =    models.CharField(_('transaction    name'),    max_length=70)
    transaction_type    =    models.CharField(_('transaction    type'),    max_length=1,    choices=TRANSACTION_TYPE_CHOICES,    default=TRANSACTION_TYPE_TRANSACTION)
    parent_transaction_id    =    models.PositiveSmallIntegerField(_('parent    transaction    id'))
    transaction_category    =    models.CharField(_('transaction    category'),    max_length=5,    choices=TRANSACTION_CATEGORY_CHOICES)
    transaction_sub_category    =    models.CharField(_('transaction    sub    category'),    max_length=8,    blank=True,    choices=TRANSACTION_SUB_CATEGORY_CHOICES)
    tranaction_config    =    models.CharField(_('url    action'),    max_length=100,    blank=False)
    create_date_time    =    models.DateTimeField(_('create    date    time'))
    mod_date_time    =    models.DateTimeField(_('modified    date    time'))
    objects    =    TransactionMasterManager()

    def    get_absolute_url(self):
        return    "/transactions/%s/"    %    urlquote(self.transaction_id)
