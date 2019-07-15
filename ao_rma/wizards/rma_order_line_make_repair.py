# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

from odoo import api, fields, models


class RmaLineMakeRepair(models.TransientModel):
    _inherit = "rma.order.line.make.repair"

    @api.model
    def _prepare_item(self, line):
        res = super(RmaLineMakeRepair, self)._prepare_item(line)
        res['type_id'] = line.operation_id.repair_type_id.id
        res['team_id'] = line.assigned_to.mrp_repair_team_id.id
        res['invoice_method'] = \
            line.operation_id.repair_type_id.invoice_method or 'none'
        return res


class RmaLineMakeRepairItem(models.TransientModel):
    _inherit = "rma.order.line.make.repair.item"

    type_id = fields.Many2one('mrp.repair.type')
    team_id = fields.Many2one('mrp.repair.team')

    @api.model
    def _prepare_repair_order(self, rma_line):
        res = super(RmaLineMakeRepairItem, self)._prepare_repair_order(
            rma_line)
        res['type_id'] = self.type_id.id
        res['team_id'] = self.team_id.id
        return res
