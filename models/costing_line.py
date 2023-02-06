from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError ,Warning


class CostingLine(models.Model):
    _name = "costing.line"
    _description = "Costing line details"
    _rec_name = 'category_id'

    cost_analysis_id = fields.Many2one("cost.analysis", string="Product Name")
    category_id = fields.Many2one("costing.category", string="Category")
    cost = fields.Float(string= "Cost")    

