# Copyright (c) 2024, kenywod.a.c@gmail.com and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.model.document import Document


class TalentProfile(Document):
    pass

def mapping():
    docusign_settings = frappe.get_doc("Docusign Settings")
    access_token = docusign_settings.access_token
    baseurl = docusign_settings.base_path
    account_id = docusign_settings.account_id
    envelopeId = "f6c46dd7-7c4c-429d-93f0-452fa49fa950"
    header = {
        "Authorization": f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    DOCUSIGN_ENVELOPE_STATUS = f"{baseurl}//v2.1/accounts/{account_id}/envelopes/{envelopeId}?include=true"
    response = ((requests.request("GET", DOCUSIGN_ENVELOPE_STATUS, headers=header)).json()).get("status")
    if response == "completed":
        DOCUSIGN_ENVELOPE_FORM_DATA = f"{baseurl}//v2.1/accounts/{account_id}/envelopes/{envelopeId}/form_data"
        form_data = (requests.request("GET", DOCUSIGN_ENVELOPE_FORM_DATA, headers=header).json()).get("formData")
        for map in form_data:
            if map['name'] == 'email_address':
                email_address = map['value']
                frappe.db.set_value("Talent Profile",f"{email_address}","email_address",email_address)