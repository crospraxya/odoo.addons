# -*- coding: utf-8 -*-
{
    'name': "Library Book",

    'summary': """
        Library Book""",


    'author': "Carlos",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/groups.xml',
         'data/data.xml',
         'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/library_book_view.xml',
        'views/library_category_view.xml'
    ],
    # only loaded in demonstration mode
    'installable':True,
}