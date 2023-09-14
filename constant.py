# -*- coding: utf-8 -*-
# Module:        constant.py
# Author:        Raks Raja - Development Team
# Description:   This module is used to initialize all the constants which will be used in Barcode generation and scanning
# Copyrights:    2020 (c) All Rights Reserved

# Python libraries
import base64


class Constant:
    #Keys for accessing Fusion API
    EMAIL = '<YOUR_EMAIL_HERE>'
    API_KEY = '<YOUR_API_KEY_HERE>'
    SUBDOMAIN = "<YOUR_SUBDOMAIN_HERE>"
    BASE_URL = "<YOUR_BASE_URL_HERE>"

    # Keys for accessing QuickBooks
    CLIENT_ID = '<YOUR_CLIENT_ID_HERE>'
    CLIENT_SECRET = '<YOUR_CLIENT_SECRET_HERE>'
    REFRESH_TOKEN = '<YOUR_REFRESH_TOKEN_HERE>'
    REDIRECT_URI = 'https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl'
    REALM_ID = '<YOUR_REALM_ID_HERE>'
    COMPANY_ID = '<YOUR_COMPANY_ID_HERE>'

    #Purchase order Constant
    #LF_PO_NUMBER = 'LA-0001'
    VendorRefName = '<YOUR_VendorRefName_HERE>'
    APAccountRefName = '<YOUR_APAccountRefName_HERE>'

    #API headers
    encoded_auth = base64.b64encode(('%s:%s' % (EMAIL, API_KEY)).encode('utf8')).decode('utf8').replace('\n', '')
    headers = {
        'Content-Type': "application/vnd.api+json",
        'x-authorization': "Bearer organization %s" % SUBDOMAIN,
        'Authorization': "Basic %s" % encoded_auth
    }
    print("Constants has been initiated!")