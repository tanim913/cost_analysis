import re
from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class ResPartner(models.Model):
    _inherit = 'purchase.order'

    cost_analysis_count = fields.Integer(string="Cost Analysis", compute='_get_calculate_cost_analysis_count')
    
    def _get_calculate_cost_analysis_count(self):
        self.cost_analysis_count = len(self.env['cost.analysis'].search([('purchase_id', '=', self.id)]))



    def view_cost_analysis_puchase_order_products(self):
        form_view_id = self.env.ref('cost_analysis.view_cost_analysis_tree')
        return {
            'type': 'ir.actions.act_window',
            'name': _('Partner Cost Analysis'),
            'res_model': 'cost.analysis',
            'view_mode': 'tree',
            'domain': [('purchase_id.id', '=', self.id)],
            'view_id': form_view_id.id,
            'context': {"create": False},
            'target': 'current'
        }
