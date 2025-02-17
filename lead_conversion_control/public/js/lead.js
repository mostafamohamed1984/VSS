frappe.ui.form.on('Lead', {
    refresh: function(frm) {
        // Get the Lead Conversion Settings
        frappe.db.get_doc('Lead Conversion Settings').then(settings => {
            if (!settings.allow_lead_conversion) {
                // Hide the entire Create button if all conversions are disabled
                frm.page.clear_actions_menu();
                return;
            }

            // Remove specific options based on settings
            frm.page.clear_actions_menu();
            
            // Only add allowed actions
            if (settings.allow_customer_conversion) {
                frm.page.add_action_item(__('Customer'), () => frm.make_customer());
            }
            
            if (settings.allow_opportunity_creation) {
                frm.page.add_action_item(__('Opportunity'), () => frm.make_opportunity());
            }
            
            if (settings.allow_quotation_creation) {
                frm.page.add_action_item(__('Quotation'), () => frm.make_quotation());
            }

            if (settings.allow_prospect_creation) {
                frm.page.add_action_item(__('Prospect'), () => frm.make_prospect());
            }
        });
    }
}); 