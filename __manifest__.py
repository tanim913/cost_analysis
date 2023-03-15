# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cost Analysis',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 3,
    'author': 'Tanim Aziz',
    'summary': 'Analyses the cost of product',
    'description': "Analyses the cost of product",
    'website': '',
    'depends': [
        'base',
        'base_setup',
        'stock',
        'purchase',
        'account'
    ],
    'data': [
        'security/security_views.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/cost_analysis_views.xml',
        'views/costing_category_views.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/purchase_order.xml',
        'views/post_expenses_views.xml',
        'security/cost_analysis_sequrity.xml',
        'report/cost_analysis_reports.xml',
        'report/cost_analysis_information_report.xml',
        
        
 
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
