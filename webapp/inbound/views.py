from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime

#import the django generic views
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView


#import the models here
from inbound.models import Supplier
from inbound.models import PurchaseOrder
from inbound.models import PurchaseOrderDtl
from item.models import ItemMaster
from inbound.models import InboundShipment
from inbound.models import InboundShipmentDtl

#import the forms
from inbound.forms import SupplierUpdateForm
from inbound.forms import PurchaseOrderUpdateForm
from inbound.forms import SupplierListForm

from django.db.models import Q
from django.core import serializers
from braces.views import JSONResponseMixin


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

# Create your views here.

##############################  Supplier Related Info  ############################
class CreateSupplier(AjaxableResponseRowMixin, CreateView):
    model = Supplier
    form_class = SupplierUpdateForm
    template_name = 'supplier/supplier_create_form.html'

    def get_success_url(self):
        return reverse('supplier-list')
        
    def get_context_data(self, **kwargs):
        context = super(CreateSupplier, self).get_context_data(**kwargs)
        context['action'] = reverse('supplier-new')
        return context
        

class UpdateSupplier(UpdateView):
    form_class = SupplierUpdateForm
    model = Supplier
    template_name = 'supplier/edit_supplier.html'

    def get_success_url(self):
        return reverse('supplier-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateSupplier, self).get_context_data(**kwargs)
        context['action'] = reverse('supplier-edit', kwargs={'pk': self.get_object().supplier_id})
        return context        

class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'supplier/delete_supplier.html'
    
    def get_success_url(self):
        return reverse('supplier-list')          
        
class ListSupplier(AjaxableResponseRowMixin, ListView):
    model = Supplier
    template_name = 'supplier/supplier_list.html'
    

##############################  Purchase Order Related Info  ############################

class ListPurchaseOrder(ListView):
    model = PurchaseOrder
    template_name = 'po/po_list.html'
    
class UpdatePurchaseOrder(UpdateView):
    model = PurchaseOrder
    template_name = 'po/edit_po.html'
    form_class = PurchaseOrderUpdateForm
    
    def get_success_url(self):
        return reverse('po-list')

    def get_context_data(self, **kwargs):
        context = super(UpdatePurchaseOrder, self).get_context_data(**kwargs)
        context['action'] = reverse('po-edit', kwargs={'pk': self.get_object().supplier_id})
        return context

def addPurchaseOrder(request):
    error = False
    suppliers = Supplier.objects.all()
    return render(request, 'po/add_po.html', {'suppliers': suppliers})
    
def createPurchaseOrder(request):
    error = False
    if ('suppliername' in request.POST and request.POST['suppliername'] != "") and ('organisationid' in request.POST and request.POST['organisationid'] != ""):
        supplier_name = request.POST['suppliername']
        organisationId = request.POST['organisationid']
        arrivalDate = request.POST['arrivaldate']
        supplier = Supplier.objects.get(name=supplier_name)
        po = PurchaseOrder(organisation_id=organisationId, supplier_id=supplier.supplier_id, expected_arrival_date=arrivalDate, status_code='CR', store_id='HATDBX001')
        po.save()
        return render(request, 'po/po_header.html', {'po': po, 'error': False})
    else:
       suppliers = Supplier.objects.all()
       return render(request, 'po/add_po.html', {'suppliers': suppliers, 'error': True})
       
def listPOWithDtls(request):
    error = False
    if ('ponbr' in request.POST and request.POST['ponbr'] != ""):
        poNbr = request.POST['ponbr']
        po = PurchaseOrder.objects.get(purchase_order_number=poNbr)
        poDtls = PurchaseOrderDtl.objects.filter(purchase_order_number=poNbr)
        return render(request, 'po/po_header_with_detail.html', {'po': po, 'poDtls': poDtls, 'error': False})
    else:
        return render(request, 'po/po_list.html', {'error': True})
   


##############################  Purchase Order Dtl Related Info  ############################

class ListPurchaseOrderDtl(ListView):
    model = PurchaseOrderDtl
    template_name = 'po/podtl_list.html'

 
def addPurchaseOrderDtl(request):
    error = False
    if ('ponbr' in request.POST and request.POST['ponbr'] != ""):
        poNbr = request.POST['ponbr']
        po = PurchaseOrder.objects.get(purchase_order_number=poNbr)
        items = ItemMaster.objects.all()
        return render(request, 'po/add_podtl.html', {'po': po, 'items': items})
    else:
        pos = PurchaseOrder.objects.all()
        return render(request, 'po/po_list.html', {'pos': pos, 'error': True}) 
        

def createPurchaseOrderDtl(request):
    error = False
    if ('ponbr' in request.POST and request.POST['ponbr'] != "") and ('dsp_sku' in request.POST and request.POST['dsp_sku'] != "") and ('orderQty' in request.POST and request.POST['orderQty'] != ""):
        poNbr = request.POST['ponbr']
        dspSku = request.POST['dsp_sku']
        order_qty = request.POST['orderQty']
        po = PurchaseOrder.objects.get(purchase_order_number=poNbr)
        item = ItemMaster.objects.get(dsp_sku=dspSku)
        poDtl = PurchaseOrderDtl(purchase_order_number=poNbr, dsp_sku=dspSku, sku_id=item.sku_id, ordered_qty=order_qty)
        poDtl.save()
        poDtls = PurchaseOrderDtl.objects.all()
        return render(request, 'po/po_header_with_detail.html', {'po': po, 'poDtls': poDtls, 'error': False})
    else:
        pos = PurchaseOrder.objects.all()
        return render(request, 'po/po_list.html', {'pos': pos, 'error': True})


##############################  Inbound Shipment Creation View  ############################

class ListInboundShipment(ListView):
    model = InboundShipment
    template_name = 'inbdshpmt/inbd_shpmt_list.html'
    
    
def ListInbdShipmentWithDtls(request):
    error = False
    if ('shpmt_nbr' in request.POST and request.POST['shpmt_nbr'] != ""):
        shipment_nbr = request.POST['shpmt_nbr']
        shipment = InboundShipment.objects.get(inbd_shipment_number=shipment_nbr)
        shipmentDtls = InboundShipmentDtl.objects.raw('SELECT * FROM inbound_inboundshipmentdtl WHERE inbd_shipment_number = %s', [shipment_nbr])
        return render(request, 'inbdshpmt/shipment_with_detail.html', {'shipment': shipment, 'shipmentDtls': shipmentDtls, 'error': False})
    else:
        return render(request, 'inbdshpmt/inbd_shpmt_list.html', {'error': True})
        
        
def addInboundShipment(request):
    error = False
    pos = PurchaseOrder.objects.all()
    return render(request, 'inbdshpmt/add_shpmt.html', {'pos': pos})
    
    
def createInboundShipment(request):
    error = False
    if('ponbr' in request.POST and request.POST['ponbr'] != ""):
        poNbr = request.POST['ponbr']
        po = PurchaseOrder.objects.get(purchase_order_number=poNbr)
        # create the inbound shipment object
        shipment = InboundShipment(organisation_id=po.organisation_id, store_id=po.store_id, purchase_order_number=po.purchase_order_number, status_code='CR')
        shipment.save()
        # create the inbound shipment details from po dtls
        poDtls = PurchaseOrderDtl.objects.raw('SELECT * FROM inbound_purchaseorderdtl WHERE purchase_order_number = %s', [poNbr])
        for poDtl in poDtls:
            shipmentDtl = InboundShipmentDtl(organisation_id=po.organisation_id, inbd_shipment_number=shipment.inbd_shipment_number, sku_id=poDtl.sku_id, dsp_sku=poDtl.dsp_sku, ordered_qty=poDtl.ordered_qty)
            shipmentDtl.save()
        # return both shipment and shipment details
        shipmentDtls = InboundShipmentDtl.objects.raw('SELECT * FROM inbound_inboundshipmentdtl WHERE inbd_shipment_number = %s', [shipment.inbd_shipment_number])
        return render(request, 'inbdshpmt/shipment_with_detail.html', {'shipment': shipment, 'shipmentDtls': shipmentDtls})
    else:
        pos = PurchaseOrder.objects.all()
        return render(request, 'inbdshpmt/add_shpmt.html', {'pos': pos})
        

# Receiving Functionality
def receiveShipment(request):
    error = False
    inbd_shpmt_nbr = request.POST['shpmnt_nbr']
    inbd_shpmt = InboundShipment.objects.get(inbd_shipment_number=inbd_shpmt_nbr)
    inbd_shpmt_dtls = InboundShipmentDtl.objects.raw('SELECT * from inbound_inboundshipmentdtl WHERE inbd_shipment_number = %s', [inbd_shpmt_nbr])
    return render(request, 'inbdshpmt/recv_shpmt.html', {'shipment': inbd_shpmt, 'shipmentDtls': inbd_shpmt_dtls})
    

def ReceiveInbdShipmentItems(request):
    error = False;
    inbd_shpmt_nbr = request.POST['shpmnt_nbr']
    dspsku = request.POST['dsp_sku']
    recvd_qty = request.POST['received_qty']
    inbd_shpmt = InboundShipment.objects.get(inbd_shipment_number=inbd_shpmt_nbr)
    inbd_shpmt_dtls  = InboundShipmentDtl.objects.raw('SELECT * from inbound_inboundshipmentdtl WHERE inbd_shipment_number = %s', [inbd_shpmt_nbr])
    for shpmtDtl in inbd_shpmt_dtls:
        if dspsku == shpmtDtl.dsp_sku:
             shpmtDtl.received_qty(recvd_qty)
    return render(request, 'inbdshpmt/recv_shpmt.html', {'shipment': inbd_shpmt, 'shipmentDtls': inbd_shpmt_dtls})
      