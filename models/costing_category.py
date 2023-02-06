from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class CostingCategory(models.Model):
    _name = "costing.category"
    _description = "Costing Category Details"
    _rec_name = 'name'

    name = fields.Char(string="Category Name")
    sequence = fields.Char(string="Sequence")

