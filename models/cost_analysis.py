from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError ,Warning


class CostAnalysis(models.Model):
    _name = "cost.analysis"
    _description = "Cost Analysis Details"
    _rec_name = 'product_id'

    product_id = fields.Many2one("product.product", string="Product Name")
    line_ids = fields.One2many('costing.line', 'cost_analysis_id', string="Cost")