# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "AO-specific customizations on Mail",
    "version": "11.0.1.1.0",
    "author": "Eficent Business and IT Consulting Services S.L.",
    "website": "http://www.eficent.com",
    "category": "Discuss",
    "depends": [
        "mail",
        "mail_debrand",
    ],
    "data": [
        "data/mail_data.xml",
        "security/res_groups.xml",
        "views/res_users_views.xml",
        "views/mail_message_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
