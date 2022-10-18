# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:26:57 2022

@author: aherva
"""

from __future__ import print_function
import gspread
#from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd
import json

SCOPE = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/drive']
SECRETS_FILE = "./scscwww-e6b31933528a.json"
SPREADSHEET = "Contact Information (Responses)"

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
#credentials = ServiceAccountCredentials(json_key['client_email'],
#                                            json_key['private_key'], SCOPE)

credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE,
                                                               SCOPE)
gc = gspread.authorize(credentials)
print("The following sheets are available")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))
    
workbook = gc.open(SPREADSHEET)
# Get the first sheet
sheet = workbook.sheet1