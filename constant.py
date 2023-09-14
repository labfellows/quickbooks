# -*- coding: utf-8 -*-
# Module:        constant.py
# Author:        Raks Raja - Development Team
# Description:   This module is used to initialize all the constants which will be used in Barcode generation and scanning
# Copyrights:    2020 (c) All Rights Reserved

# Python libraries
import base64
import os
from dotenv import load_dotenv

load_dotenv()

class Constant:
    #Keys for accessing Fusion API
    EMAIL = os.getenv("Q_EMAIL")
    API_KEY = os.getenv("Q_API_KEY")
    SUBDOMAIN = os.getenv("Q_SUBDOMAIN")
    BASE_URL = os.getenv("Q_BASE_URL")

    # Keys for accessing QuickBooks
    CLIENT_ID = os.getenv("Q_CLIENT_ID")
    CLIENT_SECRET = os.getenv("Q_CLIENT_SECRET")
    REFRESH_TOKEN = os.getenv("Q_REFRESH_TOKEN")
    REDIRECT_URI = os.getenv("Q_REDIRECT_URI")
    REALM_ID = os.getenv("Q_REALM_ID")
    COMPANY_ID = os.getenv("Q_COMPANY_ID")

    #Purchase order Constant
    #LF_PO_NUMBER = 'LA-0001'
    VendorRefName = os.getenv("Q_VendorRefName")
    APAccountRefName = os.getenv("Q_APAccountRefName")

    #API headers
    encoded_auth = base64.b64encode(('%s:%s' % (EMAIL, API_KEY)).encode('utf8')).decode('utf8').replace('\n', '')
    headers = {
        'Content-Type': "application/vnd.api+json",
        'x-authorization': "Bearer organization %s" % SUBDOMAIN,
        'Authorization': "Basic %s" % encoded_auth
    }
    print("Constants has been initiated!")