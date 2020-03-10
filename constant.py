# -*- coding: utf-8 -*-
# Module:        constant.py
# Author:        Raks Raja - Development Team
# Description:   This module is used to initialize all the constants which will be used in Barcode generation and scanning
# Copyrights:    2020 (c) All Rights Reserved

# Python libraries
import base64


class Constant:
    #Keys for accessing Fusion API
    EMAIL = 'raks+001@labfellows.com'
    API_KEY = '2fe104a07391b6a815768fc5e2a19cd5'
    SUBDOMAIN = "raks-lf"
    BASE_URL = "https://api.labfellows.org/"

    # Keys for accessing QuickBooks
    CLIENT_ID = 'ABZqsPKsVhG523iAdTgYfEeGX4R6X3vyshZ4lwrsmuddd6q8cy'
    CLIENT_SECRET = 'SMf3klmJdBuKumZyGs6shm6qXhoHK3RNwF83yrwa'
    REFRESH_TOKEN = 'AB11592484098Fn0TnhgEMLLmFNJUzw1R9S8WePMgT4TsS8QxQ'
    REDIRECT_URI = 'https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl'
    REALM_ID = '4620816365039048850'
    COMPANY_ID = '4620816365039048850'

    #Purchase order Constant
    #LF_PO_NUMBER = 'LA-0001'
    VendorRefName = 'test Python'
    APAccountRefName = 'Accounts Payable (A/P)'

    #API headers
    encoded_auth = base64.b64encode(('%s:%s' % (EMAIL, API_KEY)).encode('utf8')).decode('utf8').replace('\n', '')
    headers = {
        'Content-Type': "application/vnd.api+json",
        'x-authorization': "Bearer organization %s" % SUBDOMAIN,
        'Authorization': "Basic %s" % encoded_auth
    }
    print("Constants has been initiated!")