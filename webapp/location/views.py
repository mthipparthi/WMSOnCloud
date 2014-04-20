from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from location.models import LocationMaster
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from location.forms import LocationMasterUpdateForm
# Create your views here.

class LocationMasterView(DetailView):
    model = LocationMaster
    template_name = 'location/locn_detail.html'

class ListLocationMaster(ListView):
    model = LocationMaster
    template_name = 'location/locn_list.html'
    

class CreateLocationMaster(CreateView):
    model = LocationMaster
    template_name = 'location/edit_locn.html'
    form_class = LocationMasterUpdateForm
    
    def get_success_url(self):
        return reverse('locn-list')
        
    def get_context_data(self, **kwargs):
        context = super(CreateLocationMaster, self).get_context_data(**kwargs)
        context['action'] = reverse('locn-new')
        return context
        
        
class UpdateLocationMaster(UpdateView):
    model = LocationMaster
    template_name = 'location/edit_locn.html'
    form_class = LocationMasterUpdateForm
    
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

