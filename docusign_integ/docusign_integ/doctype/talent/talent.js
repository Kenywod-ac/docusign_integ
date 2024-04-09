// Copyright (c) 2024, kenywod.a.c@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Talent", {
	onload(frm) {
        frappe.call({
            method: "docusign_integ.docusign_integ.doctype.talent.talent.update_onboarding_packets",

            callback: function(r){
                let template_name = r.message[0]
                frm.set_df_property("onboarding_packets","options", template_name)
            }
        }),

        frappe.call({
            method: "docusign_integ.api.get_document_name",
            args: {
                "doc_name": "doc_name"
            },
            callback: function(r){
                let document_name = r.message
                frm.set_df_property("e_signature_documents","options", document_name)
            }
        })
	},

    send: function(frm){
        frappe.call({
            method: "docusign_integ.docusign_integ.doctype.talent.talent.send_envelope",
            args: {
                doc:frm.doc
            },
            callback: function(r){
                if(r.message){
                    frappe.msgprint("Envelope Sent Successfully")
                }
            }
        })
    }
});