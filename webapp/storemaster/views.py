from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import ListView


from location.models import LocationMaster
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from storemaster.forms import StoreMasterForm
from storemaster.models import StoreMaster


from django.db.models import Q
from braces.views import JSONResponseMixin
from django.core import serializers
# Create your views here.

class AjaxableResponseRowMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseRowMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        print "I am in ajax"
        response = super(AjaxableResponseRowMixin, self).form_valid(form)
        if self.request.is_ajax():
            print "Value of primary Key",self.object.pk
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response

class CreateStoreMaster(AjaxableResponseRowMixin,CreateView):
    model = StoreMaster
    template_name = 'storemaster/storemaster_create_form.html'
    form_class = StoreMasterForm

class StoreDetailView(DetailView):
    model = StoreMaster
    template_name = 'storemaster/storemaster_details.html'