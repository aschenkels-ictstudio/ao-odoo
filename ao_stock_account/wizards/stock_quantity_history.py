# Copyright 2018 Aleph Objects Inc.
# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models
from datetime import datetime


class StockQuantityHistory(models.TransientModel):
    _inherit = 'stock.quantity.history'

    def open_table(self):
        self.ensure_one()
        if self.compute_at_date:
            self.date = datetime.strptime(
                "%s %s" % (self.date_wizard, "23:59:00"),
                '%Y-%m-%d %H:%M:%S')
        action = super(StockQuantityHistory, self).open_table()
        if self.compute_at_date:
            action.update({
                'context': dict(action['context'], to_date=self.date)
            })
            tree_view_id = self.env.ref(
                'ao_stock_account.view_stock_product_tree2').id
            action['views'][0] = (tree_view_id, 'tree')
            return action
        return action
