from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class CostAnalysisTag(models.Model):
    _name = "cost.analysis.tag"
    _description = "Cost Analysis Tag Details"
    _rec_name = 'name'

    name = fields.Char(string="Tag")
    color = fields.Integer(string="Color Code")
