{
    'name': 'hospital management',
    'version': '1.0.0',
    # author: neshan dahandeye name sazandeh
    'author': 'odoo dev',
    'category': 'APP',
    # sequence: namayesh be onvane avalin app dar list
    'sequence': -1000,
    # summary: yek tosif az karkarde module hast
    'summary': 'hospital management system',
    'description': """hospital management system""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},

}

