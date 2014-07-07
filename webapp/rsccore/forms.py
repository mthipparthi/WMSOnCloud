''' ################################################################
    Base model from designed to handle the session  variable setting
    withtout much hassle. All forms will be derived from this
    ################################################################
'''

from django import forms

from crispy_forms.helper import FormHelper


# import the logger handler
import logging

class  RSCBaseForm(forms.ModelForm):
    """
       RSCBaseForm
    """
    def    __init__(self,  *args,  **kwargs):
        logger = logging.getLogger(__name__)
        logger.debug("Get the request object to handle the session variables")
        self.request = kwargs.pop("request")

        self.sessionVars = kwargs.pop("sessionvars")

        # call the base class initialization
        super(RSCBaseForm,  self).__init__(*args,    **kwargs)

        # Get the session variable list and create the corresponding element in the
        # form class
        self.session_enterprise_id = None
        self.session_store_id = None
        self.session_user_id = None

        if self.request.session['organisation_id'] is not None:
            self.session_enterprise_id = self.request.session['organisation_id']

        if self.request.session['store_id'] is not None:
            self.session_store_id = self.request.session['store_id']

        if self.request.session['user_id'] is not None:
            self.session_user_id = self.request.session['user_id']

        logger.debug("Session variables are set enterprise id is %s and store id is %s", self.session_enterprise_id, self.session_store_id)

        # set the common form related common elements here
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'


    ''' Set the session variables in the cleaned_data '''
    def clean(self):
        logger = logging.getLogger(__name__)
        logger.debug("RSCBaseForm clean method is initiated")
        for sessionVar in self.sessionVars:
            print sessionVar
            if sessionVar == 'enterprise_id':
                self.cleaned_data['enterprise_id'] = self.session_enterprise_id
            elif sessionVar == 'store_id':
                self.cleaned_data['store_id'] = self.session_store_id
            elif sessionVar == 'user_id':
                self.cleaned_data['user_id'] = self.session_user_id

        return super(RSCBaseForm, self).clean()

    ''' Add the session variable name to the list of fields '''
    def addSessionRelatedFields(self):
        for sessionVar in self.sessionVars:
            self._meta.fields.append(sessionVar)
        return True


    ''' Remove the sessions variables from the list of the fileds '''
    def clearSessionRelatedFields(self):
        logger = logging.getLogger(__name__)
        logger.debug("RSCBaseForm clearSessionRelatedFields method is initiated")
        for sessionVar in self.sessionVars:
            self._meta.fields.remove(sessionVar)
        logger.debug("RSCBaseForm clearSessionRelatedFields completed")
        return True


    class Meta:
        fields = []
