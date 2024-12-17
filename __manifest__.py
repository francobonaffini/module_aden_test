# -*- coding: utf-8 -*-
{
    'name': "Inscripciones de alumnos a programas",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
        Long description of module's purpose
    """,

    'author': "Franco Bonaffini",
    'website': "https://www.yourcompany.com",
    'category': 'Education',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/mi_modulo_security.xml',
        'security/ir.model.access.csv',
        'views/alumno_views.xml',
        'views/programa_views.xml',
        'views/inscripcion_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

