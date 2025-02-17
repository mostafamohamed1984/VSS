import frappe
from frappe.model.document import Document

class LeadConversionSettings(Document):
    def validate(self):
        if not self.allow_lead_conversion:
            # If lead conversion is disabled, ensure all sub-options are disabled
            self.allow_customer_conversion = 0
            self.allow_opportunity_creation = 0
            self.allow_quotation_creation = 0 