import re
from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError ,Warning

class ResPartner(models.Model):
    _inherit = 'res.partner'

    cost_analysis_ids = fields.One2many('cost.analysis', 'partner_id','Cost Analysis Ids')
    cost_analysis_count = fields.Integer(string="Cost Analysis Count", compute='_get_calculate_cost_analysis_count')

    @api.depends('cost_analysis_ids')
    def _get_calculate_cost_analysis_count(self):
        self.cost_analysis_count = len(self.cost_analysis_ids)

    
    