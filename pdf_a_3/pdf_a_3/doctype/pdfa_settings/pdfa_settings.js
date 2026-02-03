frappe.ui.form.on("PDFA Settings", {
	refresh(frm) {
		frm.trigger("update_ghostscript_status");
	},

	check_ghostscript(frm) {
		frappe.call({
			method: "pdf_a_3.pdf_a_3.doctype.pdfa_settings.pdfa_settings.check_ghostscript",
			callback(r) {
				if (r.message) {
					let html = "";
					if (r.message.status === "ok") {
						html = `<div class="alert alert-success">${r.message.message}</div>`;
					} else {
						html = `<div class="alert alert-danger">${r.message.message}</div>`;
					}
					frm.fields_dict.ghostscript_status.$wrapper.html(html);
				}
			},
		});
	},

	update_ghostscript_status(frm) {
		frappe.call({
			method: "pdf_a_3.pdf_a_3.doctype.pdfa_settings.pdfa_settings.check_ghostscript",
			callback(r) {
				if (r.message) {
					let html = "";
					if (r.message.status === "ok") {
						html = `<div class="alert alert-success">${r.message.message}</div>`;
					} else {
						html = `<div class="alert alert-danger">${r.message.message}</div>`;
					}
					frm.fields_dict.ghostscript_status.$wrapper.html(html);
				}
			},
		});
	},
});
