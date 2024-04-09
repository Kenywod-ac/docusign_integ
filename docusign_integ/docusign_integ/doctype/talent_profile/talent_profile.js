// Copyright (c) 2024, kenywod.a.c@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Talent Profile", {
	refresh(frm) {

	},
});

frappe.ui.form.on('Talent Task Link', {
    start(frm) {
        for(let i=0;i<10;i++){
            var redirect_url = frm.doc.task[i].url
            window.open(redirect_url, "_blank");
        }
	}	
})