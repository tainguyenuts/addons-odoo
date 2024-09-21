# __manifest__.py
{
    'name': 'My Custom Module',
    'version': '1.1',
    'category': 'Custom',
    'summary': 'Module to add custom fields',
    'description': 'This module adds custom fields to existing models.',
    'author': 'Your Name',
    'website': 'http://yourwebsite.com',
    'depends': ['base'],  # Specify dependencies here
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
    ],
    'installable': True,
    'application': False,
}

