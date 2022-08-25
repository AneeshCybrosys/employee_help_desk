# -*- coding: utf-8 -*-
{
    'name': "Employee Help Desk",

    'summary': """
        Helps to manage employee help desk""",

    'description': """
        Description
    """,

    'author': "Minions 6",

    'version': '15.0.1.0.0',
    'depends': ['hr','website'],

    'data': [
        'security/ir.model.access.csv',
        'views/website_help_desk_menu.xml',
        'views/website_help_desk_form.xml',
        'views/employee_ticket_views.xml',
        'views/employee_help_desk_menu_item.xml'],
}
