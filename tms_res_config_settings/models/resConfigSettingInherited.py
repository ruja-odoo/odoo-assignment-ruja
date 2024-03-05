from odoo import models,fields

class resConfigSettingInheritedTms(models.TransientModel):
    _inherit="res.config.settings"

    module_tms=fields.Boolean("Dispatch Management System")
