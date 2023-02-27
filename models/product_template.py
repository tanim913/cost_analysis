import re
from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class ResPartner(models.Model):
    _inherit = 'product.template'

    cost_analysis_count = fields.Integer(string="Cost Analysis", compute='_get_calculate_cost_analysis_count')
    
    def _get_calculate_cost_analysis_count(self):
        product_id = self.env['product.product'].search([('product_tmpl_id', '=', self.id)])
        # print("--------------------",len(product_id))
        # self.cost_analysis_count = len(self.env['cost.analysis'].search([('product_id', '=', product_id.id)]))
        # if len(product_id) > 1:
        #     product_id = product_id[0]
        self.cost_analysis_count = len(self.env['cost.analysis'].search([('product_id.product_tmpl_id','=',self.id)]))



    def view_cost_analysis_stock_products(self):
        tree_view_id = self.env.ref('cost_analysis.view_cost_analysis_tree')
        product_id = self.env['product.product'].search([('product_tmpl_id', '=', self.id)])
        if len(product_id) > 1:
            product_id = product_id[0]
        return {
            'type': 'ir.actions.act_window',
            'name': _('Partner Cost Analysis'),
            'res_model': 'cost.analysis',
            'view_mode': 'tree',
            'domain': [('product_id', '=', product_id.id)],
            'view_id': tree_view_id.id,
            'context': {"create": False},
            'target': 'current'
        }
