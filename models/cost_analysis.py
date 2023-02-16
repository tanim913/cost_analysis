from datetime import datetime, timedelta
from dateutil import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError ,Warning


class CostAnalysis(models.Model):
    _name = "cost.analysis"
    _description = "Cost Analysis Details"
    _rec_name = 'product_id'

    product_id = fields.Many2one("product.product", string="Product Name")
    partner_id = fields.Many2one("res.partner", string="Partner Name")
    line_ids = fields.One2many('costing.line', 'cost_analysis_id', string="Cost")
    lc_number = fields.Char(string="LC Number")
    name = fields.Char(string="Name")
    date = fields.Datetime(string="Date")
    scheduled_deadline = fields.Datetime(string="Scheduled Deadline")
    product_qty = fields.Integer(string="Product Quantity")
    lc_price = fields.Float(string= "LC Price")  
    bank_name = fields.Char(string="Bank Name")
    total_cost = fields.Float(string= "Total Cost", compute='_get_calculate_total_cost')  
    unit_cost = fields.Float(string= "Unit Cost", compute='_get_calculate_unit_cost')  
    company_code = fields.Char(string="Company Code")
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')

    @api.depends('line_ids')
    def _get_calculate_total_cost(self):
        total = 0
        for obj in self.line_ids:
            total += obj.cost
        self.total_cost = total
    
    @api.depends('line_ids','product_qty')
    def _get_calculate_unit_cost(self):
        total = 0
        for obj in self.line_ids:
            total += obj.cost 
        if self.product_qty != 0:
            self.unit_cost = total / self.product_qty
        else:
            self.unit_cost = 0
    
    def get_info(self):
        # group_id = self.env.ref("cost_analysis.group_cost_analysis_admin")
        # is_exist = False
        # for user in group_id.users:
        #     if user.id == self.env.user.id:
        #         is_exist = True
        #         break
        if self.env.user.has_group("cost_analysis.group_cost_analysis_admin"):
            raise UserError("Admin User")
        else:
            raise UserError("Logged in user  = "+ self.env.user.name)

    def company_names(self):
        records = self.env["res.partner"].search([])
        print("Total Contacts",len(records))
        company_records = records.filtered(lambda rec: rec.company_type == "company")
        company_names = company_records.mapped('name')
        str_company = "Total Company : "+str(len(company_names))+"\n\n"
        # print("-----------------Company Names------------------------")
        for name in company_names:
            str_company += str(name)+"\n"
        raise UserError(str_company)
    
    def person_names(self):
        records = self.env["res.partner"].search([])
        person_records = records.filtered(lambda rec: rec.company_type == "person")
        person_names = person_records.mapped('name')
        str_person = "Total Individual : "+str(len(person_names))+"\n\n"
        # print("-----------------Person Names------------------------")
        for name in person_names:
            str_person += str(name)+"\n"
        raise UserError(str_person)