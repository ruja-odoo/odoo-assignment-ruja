from odoo import models, fields

class VehicleModelCategory(models.Model):
    _inherit = ["fleet.vehicle.model.category"]
    max_weight=fields.Float(default=1)
    max_volume=fields.Float(default=1)

    def _compute_display_name(self):
        super()._compute_display_name()
        for record in self:
            name = record.name
            record.display_name=name+ "( " + str(record.max_weight) + "kg, " + str(record.max_volume) + "m\u00b3 )"
