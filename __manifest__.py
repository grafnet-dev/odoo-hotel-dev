{
    'name': 'Hotel Management',
    'version': '1.0',
    'author': 'Ton Nom',
    'category': 'Services',
    'summary': 'Gestion des chambres d’hôtel',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
