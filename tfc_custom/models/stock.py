# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class tfc_custom(models.Model):
#     _name = 'tfc_custom.tfc_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    #move_date = fields.Date(required=True, readonly=True, index=True, default=lambda self:self.date.date())

    def _update_reserved_quantity(self, need, available_quantity,
                                  location_id, lot_id=None,
                                  package_id=None, owner_id=None,
                                  strict=True):
        if self._context.get('sol_lot_id'):
            lot_id = self.sale_line_id.lot_id
        return super(StockMove, self)._update_reserved_quantity(
            need, available_quantity, location_id, lot_id=lot_id,
            package_id=package_id, owner_id=owner_id, strict=strict)

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        vals = super(StockMove, self)._prepare_move_line_vals(
            quantity=quantity, reserved_quant=reserved_quant)
        lot = self.sale_line_id.lot_id
        if reserved_quant and lot:
            vals['lot_id'] = lot.id
        return vals