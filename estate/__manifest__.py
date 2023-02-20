{
    'name': 'Estate',
    'application': True,
    'version': '1',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': 'Track all your building',
    'description': "This module contains all the common features of Building Management.",
    'depends': [
        'base',
        'crm',
    ],
    'data': [
        'views/realestate.xml',
        'security/ir.model.access.csv',
    ]
}

