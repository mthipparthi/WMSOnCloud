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

from sales.models import SellTransaction
from sales.models import SellTransactionDtl
from item.models import ItemMaster
from sales.forms import SellTransactionUpdateForm
from inventory.models import LocationInventory


##############################  Create Invoice Header  ############################
class CreateSellTransaction(CreateView):
    model = SellTransaction
    form_class = SellTransactionUpdateForm
    template_name = 'sales/create_sell.html'

    
    def get_success_url(self):
        return reverse('displaySell')
        
    def get_context_data(self, **kwargs):
        context = super(CreateSellTransaction, self).get_context_data(**kwargs)
        context['action'] = reverse('selltransaction-new')
        return context


def initialiseSales(request):
    error = False
    sellTrans = SellTransaction(organisation_id='HAT',store_id='HATDBX001')
    sellTrans.save()
    items = ItemMaster.objects.all()
    return render(request, 'sales/add_item.html', {'sellobject': sellTrans, 'items': items})
    
    

def sellItem(request):
    error = False
    invoice_nbr = request.POST['invoice_nbr']
    sellTrans = SellTransaction.objects.get(invoice_number=invoice_nbr)
    dspSku =  request.POST['dsp_sku']
    sold_qty =  request.POST['soldQty']
    item = ItemMaster.objects.get(dsp_sku=dspSku)
    locnInvnObj = LocationInventory.objects.get(sku_id=item.sku_id)
    sellDtl = SellTransactionDtl(invoice_number=invoice_nbr, item_barcode=item.item_barcode, qty_sold=sold_qty, sell_price=item.retail_price);
    sellDtl.save()
    invn_qty = locnInvnObj.inventory_qty
    locnInvnObj.inventory_qty = invn_qty - int(sold_qty)
    locnInvnObj.save()
    sellDtls = SellTransactionDtl.objects.filter(invoice_number=invoice_nbr)
    total_price = 0
    for sellDtl in sellDtls:
        current_sale_price = sellDtl.qty_sold * sellDtl.sell_price;
        total_price = total_price + current_sale_price
    
    # update current sale object
    sellTrans.total_amount = total_price
    sellTrans.save()
    items = ItemMaster.objects.all()
    
    return render(request, 'sales/update_sell.html', {'sellobject': sellTrans, 'items': items, 'sellDtls': sellDtls})    
