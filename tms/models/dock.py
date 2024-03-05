from odoo import models, fields

class dock(models.Model):
    _name="tms.dock"

    name=fields.Char(string="Dock")
