from django.conf.urls import patterns, include, url

from inbound import views

urlpatterns = patterns('',
    url(r'^suppliers/$', views.ListSupplier.as_view(), name='supplier-list',),
    url(r'^addSupplier/$', views.CreateSupplier.as_view(), name='supplier-new',),
    url(r'^updateSupplier/(?P<pk>\d+)/$', views.UpdateSupplier.as_view(), name='supplier-edit',),
    url(r'^deleteSupplier/(?P<pk>\d+)/$', views.DeleteSupplier.as_view(), name='supplier-remove',),
    # Purchase Order related urls
    url(r'^pos$', views.ListPurchaseOrder.as_view(), name='po-list',),
    url(r'^addPO$', views.addPurchaseOrder, name='add-po',),
    url(r'^createPO$', views.createPurchaseOrder, name='create-po',),
    url(r'^updatePO/(?P<pk>\d+)/', views.UpdatePurchaseOrder.as_view(), name='po-edit',),
    # Purchase Order Detail related urls
    url(r'^podtls$', views.ListPurchaseOrderDtl.as_view(), name='podtl-list',),
    url(r'^addPoDtl$', views.addPurchaseOrderDtl, name='add-podtl',),
    url(r'^createPoDtl$', views.createPurchaseOrderDtl, name='create-podtl',),
    url(r'^ListPoWithDtls$', views.listPOWithDtls, name='listPoWithDtl',),
    url(r'^ListPurchaseOrder$', views.ListPurchaseOrder.as_view(), name='po_list',),
    # Shipment Detail
    url(r'^addInboundShipment$', views.addInboundShipment, name='add_inbdshpmt',),
    url(r'^createInboundShipment$', views.createInboundShipment, name='create_inbdshpmt'),
    # Receiving
    url(r'^listInboundShipment$', views.ListInboundShipment.as_view(), name='list_inbdshipment',),
    url(r'^listInbdShipmentWithDtls$', views.ListInbdShipmentWithDtls, name='listShipmentDtl',),
    url(r'^receiveShipment$', views.receiveShipment, name='receive_inbd_shipment'),
    url(r'^receiveInbdShipmentItems$', views.ReceiveInbdShipmentItems, name='recv_item',),
    
)