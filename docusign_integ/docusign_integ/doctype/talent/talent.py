# Copyright (c) 2024, kenywod.a.c@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json
import base64
from docusign_integ.api import get_template_name_id

class Talent(Document):
    pass

@frappe.whitelist()
def update_onboarding_packets():
    templates = get_template_name_id()
    template_name = [template["name"] for template in templates]
    template_id = [template["templateId"] for template in templates]
    return template_name,template_id

@frappe.whitelist()
def send_envelope(doc):
    data = json.loads(doc)
    templates = update_onboarding_packets()
    template_ids = templates[1]
    template_id = template_ids[templates[0].index(str(data.get("onboarding_packets")))]
    email_id = data.get("job_applicant")
    from docusign_integ.api import  create_envelope, update_doc_to_envelope
    envelope_id = create_envelope(template_id)
    name = ((data.get("e_signature_documents")).split("."))[0]
    extension = ((data.get("e_signature_documents")).split("."))[1]
    file_name = data.get("e_signature_documents")
    documentid = 1
    with open(f'/home/kenywod/Downloads/{file_name}', 'rb') as file:
        encoded_string = base64.b64encode(file.read()).decode('ascii')

    url_link = update_doc_to_envelope(envelope_id, encoded_string, name, extension, documentid, email_id)
    url_data = json.loads(url_link)
    url = url_data.get("url")
    talent_profile = frappe.get_doc("Talent Profile", email_id)
    data = {
        "task_name": f"{file_name}",
        "url": f"{url}",
    }
    talent_profile.append("task",data)
    talent_profile.save()
    
    return "Sent"
