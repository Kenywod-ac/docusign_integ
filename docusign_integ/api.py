import frappe
import requests
import json
from frappe.utils import cstr

def get_access_token():
    docusign_settings = frappe.get_doc("Docusign Settings")
    refresh_token = docusign_settings.refresh_token
    encoded_keys = docusign_settings.encoded_keys
    hostenv = docusign_settings.hostenv
    DOCUSIGN_AUTH_URL = f'https://{hostenv}/oauth/token' 
    header = {
        "Authorization": f"Basic {encoded_keys}",
        'Content-Type': 'application/x-www-form-urlencoded',
        "Connection": "keep-alive"
    }
    payload = f'refresh_token={refresh_token}&grant_type=refresh_token'
    response = requests.request("POST", DOCUSIGN_AUTH_URL, headers=header, data=payload)
    access_token = json.loads(response.text)["access_token"]
    frappe.db.set_value("Docusign Settings","Docusign Settings", "access_token", access_token)
    
def get_template_name_id():
    docusign_settings = frappe.get_doc("Docusign Settings")
    access_token = docusign_settings.access_token
    baseurl = docusign_settings.base_path
    account_id = docusign_settings.account_id
    header = {
        "Authorization": f"Bearer {access_token}",
        'Accept': 'application/json',
    }
    DOCUSIGN_TEMPLATE_URL = f"{baseurl}//v2.1/accounts/{account_id}/templates"
    response = requests.request("GET", DOCUSIGN_TEMPLATE_URL, headers=header)
    templates = json.loads(response.text)
    template_info = [{'templateId': template['templateId'], 'name': template['name']} for template in templates['envelopeTemplates']]
    
    return template_info    
    
@frappe.whitelist()        
def get_document_name(doc_name = None):
    docusign_settings = frappe.get_doc("Docusign Settings")
    access_token = docusign_settings.access_token
    baseurl = docusign_settings.base_path
    account_id = docusign_settings.account_id
    header = {
        "Authorization": f"Bearer {access_token}",
        'Accept': 'application/json',
    }
    template = get_template_name_id()
    template_ids = [template["templateId"] for template in template]
    document_names = []
    doc_details =[]
    for template_id in template_ids:
        DOCUSIGN_TEMPLATE_URL = f"{baseurl}//v2.1/accounts/{account_id}/templates/{template_id}"        
        response = requests.request("GET", DOCUSIGN_TEMPLATE_URL, headers=header)
        doc_detail = json.loads(response.text)
        doc_details.append(doc_detail)
        document_name_with_extension = json.loads(response.text)["documents"][0]["name"]
        document_names.append(document_name_with_extension)
    
    if doc_name:
        return document_names
    
    return doc_details


def create_envelope(template_id):
    docusign_settings = frappe.get_doc("Docusign Settings")
    access_token = docusign_settings.access_token
    baseurl = docusign_settings.base_path
    account_id = docusign_settings.account_id
    header = {
        "Authorization": f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
    "emailBlurb": "An envelope needs signing!",
    "emailSubject": "Signing request",
    "status": "created",
    "templateRoles": [
        {
        "name": "Sam",
        "email": "kenywod@riverstonetech.in",
        "routingOrder": "1",
        "roleName": "DocuSign Admin"
        }
    ],
    "compositeTemplates": [{
        "serverTemplates": [{
        "sequence": "1",
        "templateId": f"{template_id}"
        }]
    }]

    })
    DOCUSIGN_ENVELOPE_URL = f"{baseurl}//v2.1/accounts/{account_id}/envelopes"
    response = requests.request("POST", DOCUSIGN_ENVELOPE_URL, headers=header, data=payload)
    envelope_id = json.loads(response.text)["envelopeId"]
    return envelope_id
    
def update_doc_to_envelope(envelope_id, docbase64, name, extension, documentid, email_id):
    docusign_settings = frappe.get_doc("Docusign Settings")
    access_token = docusign_settings.access_token
    baseurl = docusign_settings.base_path
    account_id = docusign_settings.account_id
    header = {
        "Authorization": f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload1 = json.dumps({
        "documents": [
            {
            "documentBase64": f"{docbase64}",
            "name": f"{name}",
            "fileExtension": f"{extension}",
            "documentId": f"{documentid}"
            } ]    
    })
    envelopeId = envelope_id
    DOCUSIGN_EVNELOPE_DOC_URL = f"{baseurl}//v2.1/accounts/{account_id}/envelopes/{envelopeId}/documents"
    requests.request("PUT", DOCUSIGN_EVNELOPE_DOC_URL, headers=header, data=payload1)
    payload2 = json.dumps({
        "signers": [
            {
            "email": f"{email_id}",
            "name": "Raj",
            "recipientId": "1"
            }
        ]
    })
    DOCUSIGN_EVNELOPE_REP_URL = f"{baseurl}//v2.1/accounts/{account_id}/envelopes/{envelopeId}/recipients"
    requests.request("PUT", DOCUSIGN_EVNELOPE_REP_URL, headers=header, data=payload2)
    payload3 = json.dumps({

        "status": "sent"

    })
    DOCUSIGN_EVNELOPE_SEND_URL = f"{baseurl}//v2.1/accounts/{account_id}/envelopes/{envelopeId}?resend_envelope=true"
    requests.request("PUT", DOCUSIGN_EVNELOPE_SEND_URL, headers=header, data=payload3)
    payload4 = json.dumps({

            "authenticationMethod": "none",
            "email": f"{email_id}",
            "recipientId": "1",
            "returnUrl":"http://localhost:8000/app/talent-profile/kenywod.a.c%40gmail.com",
            "userName": "Raj"  

    })
    DOCUSIGN_EVNELOPE_SEND_URL = f"{baseurl}//v2.1/accounts/{account_id}/envelopes/{envelopeId}/views/recipient"
    response = requests.request("POST", DOCUSIGN_EVNELOPE_SEND_URL, headers=header, data=payload4)
    
    return response.text    
    
def attach():
    envelopeId = "ec784b8b-c8a6-4f6c-a57b-11d73df1c71a"
    docusign_settings = frappe.get_doc("Docusign Settings")
    access_token = docusign_settings.access_token
    baseurl = docusign_settings.base_path
    account_id = docusign_settings.account_id
    header = {
        "Authorization": f"Bearer {access_token}",
        'Content-Type': 'application/pdf',
    }
    DOCUSIGN_EVNELOPE_DOWN_URL = f"{baseurl}//v2.1/accounts/{account_id}/envelopes/{envelopeId}/documents/combined"
    response = requests.request("GET", DOCUSIGN_EVNELOPE_DOWN_URL, headers=header)
    site = str(cstr(frappe.local.site))
    file_path = "/private/files/eep_form_raj.pdf"
    with open(site+file_path, "wb") as file:
        file.write(response.content)
    
    attach_file = frappe.new_doc("File")
    attach_file.attached_to_doctype = "Talent Profile"
    attach_file.attached_to_name = "kenywod.a.c@gmail.com"
    attach_file.folder = "Home"
    attach_file.file_name = "W4_raj.pdf"
    attach_file.file_url = file_path
    attach_file.is_private = 1
    attach_file.insert(ignore_permissions=True)
    attach_file.save()
    frappe.db.commit()
    

    

