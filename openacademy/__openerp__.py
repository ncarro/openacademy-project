# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Sisinfo",
    'website': "http://sisinfo.uy",

    # Categories can be used to filter modules in modules listing
    #
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'view/openacademy_course_view.xml',
        'view/openacademy_session_view.xml',
        'view/partner.xml',
        'workflow/openacademy_session_workflow.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'view/openacademy_session_wizard.xml',
        'view/session_board.xml',
        'report/openacademy_session_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],
    'installable': True,
}
