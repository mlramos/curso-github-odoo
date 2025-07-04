# -*- coding: utf-8 -*-
{
    'name': "Infinityloop",

    'summary': """
       Módulo de ejemplo para el curso de Odoo""",
       
    'description': """
        Este es un módulo de ejemplo para el curso de Odoo. 
       
    """,

    'author': "Infinityloop",
    'website': "http://www.infinityloop.es",
    'category': 'tools',
    'version': '16.0.1.0.0',
    'depends': ['base','stock','sale','purchase','account'],

    # always loaded
    'data': [
        'data/data_server_action.xml',
        'views/res_partner_views.xml',   
    ],
    
}