# -*- coding: utf-8 -*-
{
    'name': 'Sales Management Users',
    'description': """ All types of users whom are related to activities of Sales Management""",
    "author": "Genweb2 Limited",
    "website": "http://www.genweb2.com",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    'category': 'Sales',
    'depends': [
        'base',
        'sale',
        'sales_team',
    ],
    'data': [
        'security/users.xml',
    ],
    'installable': True,
}

