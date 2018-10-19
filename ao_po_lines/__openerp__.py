# -*- coding: utf-8 -*-
# Copyright 2015-18 Eficent Business and IT Consulting Services S.L.
# - Héctor Villarreal Ortega
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "AO Purchase Order Lines Invoicing Status",
    "version": "9.0.1.0.0",
    "author": "Eficent",
    "website": "http://www.eficent.com",
    "category": "Purchase",
    "depends": ["purchase",
                "account",
                ],
    "data": [
        "views/purchase_order_line_view.xml",
    ],
    "license": "AGPL-3",
    'installable': True,
}
