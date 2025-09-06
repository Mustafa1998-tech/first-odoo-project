{
    'name': 'Customer Management',
    'version': '1.0',
    'summary': 'Manage customers easily',
    'description': 'This module allows you to manage customers in Odoo.',
    'author': 'Mustafa Ahmed',
    'category': 'Sales',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/customer_data.xml',
        'views/customer_views.xml',
    ],
    'installable': True,
    'application': True,
}
