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
        'base_setup',
        'stock'
    ],
    'data': [
    
        'security/ir.model.access.csv',
        'views/cost_analysis_views.xml',
        'views/costing_category_views.xml',
 
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
