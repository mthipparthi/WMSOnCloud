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

from location.forms import LocationMasterCreateForm
from location.forms import LocationSearchForm

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



class LocationMasterView(DetailView):
    model = LocationMaster
    template_name = 'location/locn_detail.html'

class ListLocationMaster(ListView):
    model = LocationMaster
    template_name = 'location/locn_list.html'


class CreateLocationMaster(AjaxableResponseRowMixin,CreateView):
    model = LocationMaster
    template_name = 'location/location_create_form.html'
    form_class = LocationMasterCreateForm

class UpdateLocationMaster(UpdateView):
    model = LocationMaster
    template_name = 'location/edit_locn.html'
    form_class = LocationMasterCreateForm

    def get_success_url(self):
        return reverse('locn-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateLocationMaster, self).get_context_data(**kwargs)
        context['action'] = reverse('locn-edit', kwargs={'pk': self.get_object().location_id})
        return context


class DeleteLocationMaster(DeleteView):
    model = LocationMaster
    template_name = 'location/delete_locn.html'

    def get_success_url(self):
        return reverse('locn-list')

def LocationSearchView(request):
    print "LocationSearchView"
    if request.method == 'POST':
        form = LocationSearchForm(request.POST)
        if form.is_valid():
            organisation_id = request.POST.get('organisation_id',    '')
            store_id = request.POST.get('store_id',    '')
            condition = Q(organisation_id=organisation_id) \
                    | Q(store_id=store_id)

            locations_list = LocationMaster.objects.filter(condition)
            data = serializers.serialize("json", locations_list)
            response_kwargs={}
            response_kwargs['content_type'] = 'application/json'
            print data
            return HttpResponse(data, **response_kwargs)
    else:
        form = LocationSearchForm()
    return render(request,'location/location_search_list_form.html',{'form':form,})

class LocationDetailView(DetailView):
    model = LocationMaster
    template_name = 'location/location_detail_form.html'