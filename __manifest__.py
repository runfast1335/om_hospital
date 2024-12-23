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
    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/appooiment_view.xml',
        'views/female_patient_view.xml',
        'views/patient_view.xml',
        'views/patient_tag_view.xml',
        'views/menu.xml',
        'data/paperformat.xml',
        'report/report_total_patient.xml',
        'report/report_inherit_patient.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},

}


