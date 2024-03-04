from odoo import models,fields,api

class tmsStockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle=fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category=fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")
    weight=fields.Float(compute="_compute_weight",store=True)
    volume=fields.Float(compute="_compute_volume",store=True)
    total_transfers=fields.Integer(compute="_compute_transfers",store=True, string="Transfers")
    total_lines=fields.Integer(compute="_compute_lines",store=True)

    @api.depends("picking_ids")
    def _compute_transfers(self):

        for record in self:
            record.total_transfers=len(record.picking_ids)

    @api.depends("move_line_ids")
    def _compute_lines(self):

        for record in self:
            record.total_lines=len(record.move_line_ids)

    @api.depends("move_ids")
    def _compute_weight(self):

        for record in self:
            totalweight=0

            for move_id in record.move_ids:
                print(move_id.product_qty)
                print(move_id.product_id.weight)
                totalweight=totalweight+move_id.product_qty*move_id.product_id.weight
            print(totalweight)
            print(record.vehicle_category.max_weight)
            if record.vehicle_category.max_weight<=0:
                record.weight=totalweight*100
            else:
                record.weight=(totalweight/record.vehicle_category.max_weight)*100
            if record.weight>100:
                record.weight=100

    @api.depends("move_ids")
    def _compute_volume(self):

        for record in self:
            totalvolume=0
            for move_id in record.move_ids:
                print(move_id.product_qty)
                print(move_id.product_id.volume)
                totalvolume=totalvolume+move_id.product_qty*move_id.product_id.volume
            print(totalvolume)
            print(record.vehicle_category.max_volume)
            if record.vehicle_category.max_volume<=0:
                record.volume=(totalvolume)*100
            else:
                record.volume=(totalvolume/record.vehicle_category.max_volume)*100
            # if record.volume>100:
            #     record.volume=100
