from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from item.models import ItemMaster
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from item.forms import ItemMasterCreateForm
from item.forms import ItemMasterUpdateForm
from item.forms import ItemLocationAssignmentForm
from item.forms import ItemSearchForm
from location.models import LocationMaster

from django.db.models import Q
from braces.views import JSONResponseMixin
from django.core import serializers

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

#logging handler
import logging

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



class ItemMasterView(DetailView):
    model = ItemMaster
    template_name = 'item/item_detail_form.html'

class ListItemMater(ListView):
    model = ItemMaster
    template_name = 'item/item_list.html'


class CreateItemMater(AjaxableResponseRowMixin,CreateView):
    model = ItemMaster
    template_name = 'item/item_create_form.html'
    form_class = ItemMasterCreateForm


class UpdateItemMaster(UpdateView):
    model = ItemMaster
    template_name = 'item/edit_item.html'
    form_class = ItemMasterUpdateForm

    def get_success_url(self):
        return reverse('item-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateItemMaster, self).get_context_data(**kwargs)
        context['action'] = reverse('item-edit', kwargs={'pk': self.get_object().sku_id})
        return context


class DeleteItemMaster(DeleteView):
    model = ItemMaster
    template_name = 'item/delete_item.html'

    def get_success_url(self):
        return reverse('item-list')


def searchItem(request):
    error = False
    logger = logging.getLogger(__name__)
    logger.debug('Item Name searched is %s', request.POST['item_name'])
    if ('item_name' in request.POST and request.POST['item_name'] != "") or ('item_barcode' in request.POST and request.POST['item_barcode'] != "") or ('item_description' in request.POST and request.POST['item_description'] != "") :
        form = ItemSearchForm(request.POST)
        if form.is_valid():
            itemname = request.POST.get('item_name', '')
            itembarcode= request.POST.get('item_barcode', '')
            itemdesc = request.POST.get('item_description', '')
            if itemname != '':
                item_list = ItemMaster.objects.filter(item_name=itemname)
            elif itembarcode != '':
                item_list = ItemMaster.objects.filter(item_barcode=itembarcode)
            elif itemdesc != '':
                itemdescription = '%';
                itemdescription += itemdesc
                itemdescription += '%'
                item_list = ItemMaster.objects.raw('SELECT * FROM item_itemmaster WHERE item_description like %s', [itemdescription])
            return render(request, 'item/item_search_list.html', {'item_list': item_list})
    else:
        error = True
        return render(request, 'item/item_search_list.html', {'error': error})

def ItemSearchView(request):
    print "ItemSearchView"
    logger = logging.getLogger(__name__)
    logger.debug('Item Name searched is %s', request.POST['item_name'])
    if request.method == 'POST':
        form = ItemSearchForm(request.POST)
        if form.is_valid():
            item_name = request.POST.get('item_name',    '')
            item_barcode = request.POST.get('item_barcode',    '')
            item_description = request.POST.get('item_description',    '')
            condition = Q(item_name=item_name) \
                    | Q(item_barcode=item_barcode) \
                    | Q(item_description=item_description)

            items_list = ItemMaster.objects.filter(condition)
            data = serializers.serialize("json", items_list)
            response_kwargs={}
            response_kwargs['content_type'] = 'application/json'
            print data
            return HttpResponse(data, **response_kwargs)
    else:
        form = ItemSearchForm()
    return render(request,'item/item_search_list_form.html',{'form':form,})

def AssignLocationSearch(request):
    if request.method == 'POST':
        form = ItemLocationAssignmentForm(request.POST)
        if form.is_valid():
            sku_id = request.POST.get('item_name',    '')
            dsp_location = request.POST.get('item_barcode',    '')
            data = {'Success' : 'SUCCESS'}
            response_kwargs={}
            response_kwargs['content_type'] = 'application/json'
            print data
            return HttpResponse(data, **response_kwargs)
    else:
        locns = LocationMaster.objects.all()
        items = ItemMaster.objects.all()
        form = ItemLocationAssignmentForm()
    return render(request,'item/item_locn_assign_form.html',{'form':form,'locns':locns,'items':items})
