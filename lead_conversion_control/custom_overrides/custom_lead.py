import frappe
from frappe import _
from erpnext.crm.doctype.lead.lead import Lead

class CustomLead(Lead):
    def before_validate(self):
        super().before_validate()
        self.validate_conversion_permissions()

    def validate_conversion_permissions(self):
        if self.status == "Converted":
            # Get settings from Custom DocType (we'll create this later)
            settings = frappe.get_doc("Lead Conversion Settings")
            
            if not settings.allow_lead_conversion:
                frappe.throw(_("Lead conversion is not allowed as per system settings."))

    def make_customer(self):
        if not self.can_convert_to("Customer"):
            frappe.throw(_("Converting lead to Customer is not allowed."))
        return super().make_customer()

    def make_opportunity(self):
        if not self.can_convert_to("Opportunity"):
            frappe.throw(_("Creating Opportunity from lead is not allowed."))
        return super().make_opportunity()

    def make_quotation(self):
        if not self.can_convert_to("Quotation"):
            frappe.throw(_("Creating Quotation from lead is not allowed."))
        return super().make_quotation()

    def can_convert_to(self, doctype):
        settings = frappe.get_doc("Lead Conversion Settings")
        conversion_map = {
            "Customer": "allow_customer_conversion",
            "Opportunity": "allow_opportunity_creation",
            "Quotation": "allow_quotation_creation"
        }
        return getattr(settings, conversion_map.get(doctype, ""), 0) 