import re
from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cost_analysis_ids = fields.One2many('cost.analysis', 'partner_id', 'Cost Analysis Ids')
    cost_analysis_count = fields.Integer(string="Cost Analysis Count", compute='_get_calculate_cost_analysis_count')

    @api.depends('cost_analysis_ids')
    def _get_calculate_cost_analysis_count(self):
        self.cost_analysis_count = len(self.cost_analysis_ids)

    def view_cost_analysis_products(self):
        form_view_id = self.env.ref('cost_analysis.view_cost_analysis_tree')
        return {
            'type': 'ir.actions.act_window',
            'name': _('Partner Cost Analysis'),
            'res_model': 'cost.analysis',
            'view_mode': 'tree',
            'domain': [('partner_id.id', '=', self.id)],
            'view_id': form_view_id.id,
            'context': {"create": False},
            'target': 'current'
        }
