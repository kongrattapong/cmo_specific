# -*- coding: utf-8 -*-
{
    "name": "CMO :: Account Extension",
    "summary": "",
    "version": "1.0",
    "category": "Accounting & Finance",
    "description": """
    """,
    "website": "http://ecosoft.co.th",
    "author": "Tharathip C., Phongyanon Y.",
    "license": "AGPL-3",
    "depends": [
        'account',
        'account_voucher',
        'account_operating_unit',
        'hr_expense_advance_clearing',
        'sale_layout',
        'project',
    ],
    "data": [
        'wizard/account_tax_detail_view.xml',
        'wizard/edit_desc.xml',
        'views/product_view.xml',
        'views/account_view.xml',
        'views/account_voucher_view.xml',
    ],
    "application": False,
    "installable": True,
}
