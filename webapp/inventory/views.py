from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime


from inventory.models import LocationInventory
from item.models import ItemMaster
from location.models import LocationMaster
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from inventory.forms import LocationInventoryUpdateForm
from inventory.forms import LocationInventorySearchForm

# Create your views here.
class LocationInventoryView(DetailView):
    model = LocationInventory
    template_name = 'inventory/locnInventory_detail.html'

class ListLocationInventory(ListView):
    model = LocationInventory
    template_name = 'inventory/locnInventory_list.html'
    

class UpdateLocationInventory(UpdateView):
    model = LocationInventory
    template_name = 'inventory/edit_locnInventory.html'
    form_class = LocationInventoryUpdateForm
    
    def get_success_url(self):
        return reverse('locnInventory-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateLocationInventory, self).get_context_data(**kwargs)
        context['action'] = reverse('locninventory-edit', kwargs={'pk': self.get_object().id})
        return context


class DeleteLocationInventory(DeleteView):
    model = LocationInventory
    template_name = 'inventory/delete_locnInventory.html'
    
    def get_success_url(self):
        return reverse('locnInventory-list')
        

def AssignLocation(request):
    if('skuid' in request.POST and request.POST['skuid']!= "" and
       'dsplocn' in request.POST and request.POST['dsplocn']!= ""):
        displayLocn = request.POST['dsplocn']
        item = ItemMaster.objects.get(pk=request.POST.get('skuid'))
        locn = LocationMaster.objects.get(dsp_location=displayLocn)
        locnInventory = LocationInventory(location_id=locn.location_id, organisation_id='HAT', store_id='HATDBX001', dsp_location=locn.dsp_location, sku_id=item.sku_id, dsp_sku=item.dsp_sku, last_sell_datetime=datetime.now())
        locnInventory.save()
        locnInventorys = LocationInventory.objects.all()
        return render(request, 'inventory/locnInventory_list_with_input.html', {'locnInventorys': locnInventorys, 'error': False})
    else:
        return render(request, 'inventory/locnInventory_list.html', {'error': True})
        

def searchLocationInventory(request):
    error = False
    if ('dspsku' in request.POST and request.POST['dspsku'] != "") or ('dsplocn' in request.POST and request.POST['dsplocn'] != ""):     
        form = LocationInventorySearchForm(request.POST)
        if form.is_valid():
            dsp_sku = request.POST.get('dspsku', '')
            dsp_locn= request.POST.get('dsplocn', '')
            if dsp_sku != '':
                locninventory_list = ItemMaster.objects.raw('SELECT * FROM inventory_locationinventory WHERE dsp_sku = %s', [dsp_sku])
            elif dsp_locn != '':
                locninventory_list = ItemMaster.objects.raw('SELECT * FROM inventory_locationinventory WHERE dsp_location = %s', [dsp_locn])
            return render(request, 'inventory/locnInventory_list_with_input.html', {'locnInventorys': locninventory_list})
    else:
       error = True
       return render(request, 'inventory/locnInventory_list_with_input.html', {'error': error})