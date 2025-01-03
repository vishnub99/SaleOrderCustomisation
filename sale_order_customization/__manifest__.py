# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Customization',
    'version': '17.0.1.0',
    'category': 'Sale',
    'author': '',
    'website': "",
    'description': """
        -Sale order customization.
    """,
    'depends': ['base','sale','stock','sale_stock','account','sales_team'],
    'data': [
        'security/sale_security.xml',
        'views/sale_order_view.xml',
        'views/res_config_view.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
