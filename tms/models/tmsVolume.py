from odoo import models,fields,api

class tmsStockPickingBatch(models.Model):
    _inherit = "stock.picking"

    totalVolume=fields.Float(compute="_compute_total_volume")

    @api.depends("move_ids")
    def _compute_total_volume(self):
        for record in self:
            vol=0
            for move_id in record.move_ids:
                vol=vol+move_id.product_qty*move_id.product_id.volume
            record.totalVolume=vol