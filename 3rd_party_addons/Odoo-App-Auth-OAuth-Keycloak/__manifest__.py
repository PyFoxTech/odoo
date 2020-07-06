# -*- coding: utf-8 -*-
{
    'name': "Auth OAuth Keycloak",

    'summary': """
        Enables Keycloack integration for the OAuth2 Authentication module.""",

    'description': """
        Enables Keycloack integration for the OAuth2 Authentication module.
    """,

    'author': "Mint System",
    'website': "https://www.mint-system.ch",

    'category': 'Technical Settings',
    'version': '1.0.0',

    'depends': [
        'base',
        'auth_oauth',
    ],

    'data': [
        'views/ir_model_fields.xml',
        'views/ir_ui_view.xml',
    ],
}
