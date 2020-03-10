# -*- coding: utf-8 -*-
# Module:        purchase_order.py
# Author:        Raks Raja - Development Team
# Description:   This module is used to read the purchase order from LF API and create the same purchase order in Quickbooks
# Copyrights:    2020 (c) All Rights Reserved

# Python Libraries
import requests
from quickbooks import QuickBooks
from intuitlib.client import AuthClient
from constant import Constant
from quickbooks.objects.purchaseorder import PurchaseOrder
from quickbooks.objects.vendor import Vendor
from quickbooks.objects.customer import Customer
from quickbooks.objects.item import Item
from quickbooks.objects.base import Ref
from quickbooks.objects.detailline import ItemBasedExpenseLine, ItemBasedExpenseLineDetail

# Setup an AuthClient
auth_client = AuthClient(
    client_id=Constant.CLIENT_ID,
    client_secret=Constant.CLIENT_SECRET,
    environment='sandbox',
    redirect_uri=Constant.REDIRECT_URI,
)
# Setup QuickBooks client object
client = QuickBooks(
    auth_client=auth_client,
    refresh_token=Constant.REFRESH_TOKEN,
    company_id=Constant.COMPANY_ID,
)

class PurchaseOrder:

    def create_qb_purchase_order(get_lf_po):
        """Gets input from LF Purchase order API and creates purchase order in Quickbooks"""
        try:
            lf_po_json = get_lf_po.json()
            requisition_id = lf_po_json['data'][0]['requisition_id']
            requisition_url = Constant.BASE_URL + 'v2/requisitions/%s' % (requisition_id)
            get_requisitions = requests.get(requisition_url, headers=Constant.headers)
            if get_requisitions.status_code != 200:
                print('An exception has occured while processing the API request for the requisition ID %s: %s %s' % (requisition_id, get_requisitions.status_code, get_requisitions.reason))
                return False
            requisition_json = get_requisitions.json()
            lf_po = requisition_json['purchase_orders'][0]
            lf_po_lines = requisition_json['purchase_orders'][0]['lines']
            qb_po = PurchaseOrder()
            qb_po.VendorRef = Ref()
            qb_po.VendorRef.value = Vendor.where("DisplayName LIKE '{}%'".format(Constant.VendorRefName), qb=client)[0].Id
            qb_po.APAccountRef = Ref()
            qb_po.APAccountRef.value = "33"
            qb_po.DocNumber =  lf_po['po_number']
            existing_qb_po = PurchaseOrder.where("DocNumber LIKE '{}'".format(lf_po['po_number']), qb=client)
            if existing_qb_po: # check for any same purchase order existing in Quickbooks to avoid duplication
                print("There was already a purchase order existing in Quickbooks for the PO Number %s" % (lf_po['po_number']))
                return False
            # Finding the item reference from QuickBooks
            item_ref_list = []
            for item_ref in Item.all(qb=client):
                if item_ref.Taxable and item_ref.PurchaseCost > 0:
                    item_ref_list.append(item_ref)
            if len(item_ref_list) < 1:
                print("There is no valid item reference found from Quickbooks for the PO Number %s" % (lf_po['po_number']))
                return False
            # preparing purchase order lines
            for line in lf_po_lines:
                detail_line = ItemBasedExpenseLine()
                detail_line.ItemBasedExpenseLineDetail = ItemBasedExpenseLineDetail()
                unit_price = line['item']['price_in_cents']/100
                qty = line['quantity_requested']
                detail_line.Amount = unit_price * qty
                detail_line.LineNum = 1
                detail_line.Description = line['item']['name']
                detail_line.ItemBasedExpenseLineDetail.BillableStatus = "Billable"
                detail_line.ItemBasedExpenseLineDetail.UnitPrice = unit_price
                detail_line.ItemBasedExpenseLineDetail.Qty = qty
                detail_line.ItemBasedExpenseLineDetail.Qty = qty
                detail_line.ItemBasedExpenseLineDetail.CustomerRef = Ref()
                detail_line.ItemBasedExpenseLineDetail.CustomerRef.value = Customer.all(qb=client)[0].Id
                detail_line.ItemBasedExpenseLineDetail.ItemRef = Ref()
                detail_line.ItemBasedExpenseLineDetail.ItemRef.value = item_ref_list[0].Id
                qb_po.Line.append(detail_line)
            qb_po.save(qb=client) # creating purchase order in QuickBooks
            print("A purchase order %s has been successfully created in Quickbooks." % (lf_po['po_number']))
        except Exception as exception:
            print('An exception has occured: ' + str(exception))

    all_purchase_order_url = Constant.BASE_URL + 'v2/purchase_orders'
    get__all_lf_po = requests.get(all_purchase_order_url, headers=Constant.headers)
    if get__all_lf_po.status_code != 200:
        print('An exception has occured while processing the API request: %s %s' % (get__all_lf_po.status_code, get__all_lf_po.reason))
    for lf_po_data in get__all_lf_po.json()['data']: # Looping all the purchase order's from LF
        lf_po_number = lf_po_data['po_number']
        purchase_order_url = Constant.BASE_URL + 'v2/purchase_orders?filter=%s' % (lf_po_number)
        get_lf_po = requests.get(purchase_order_url, headers=Constant.headers)
        if get_lf_po.status_code != 200:
            print('An exception has occured while processing the API request for LF Po number %s: %s %s' % (lf_po_number, get_lf_po.status_code, get_lf_po.reason))
            break
        create_qb_purchase_order(get_lf_po)