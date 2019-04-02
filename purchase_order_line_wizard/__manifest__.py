# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Wizard",

    'summary': """
        Purchase Order Wizard""",


    'author': "Carlos",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
         'views/purchase_order_line_wizard.xml',
    ],
    # only loaded in demonstration mode
    'installable':True,
}