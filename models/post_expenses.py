from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class PostExpenses(models.Model):
    _name = "post.expenses"
    _description = "Post Expenses Details"
    _rec_name = 'journal'

    date = fields.Date(string="Date")
    journal = fields.Many2one("account.journal", string="Journal")
    reference = fields.Char(string="Reference")
    amount = fields.Float(string="Amount")
    
