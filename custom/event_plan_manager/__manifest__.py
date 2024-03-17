{
    "name": "Event Manager",
    "version": "1.0.0",
    'author': "Terabits Technolab",
    'summary': """   Event Manager
    """,
    'description': """ 
        Module For Event planning manager.
    """,
    "sequence": 7,
    "license": "OPL-1",
    "category": "Management/Managing",
    "website": "https://www.verniy.xyz",
    "depends": ["base", "clarity_backend_theme_bits"],
    "data": [
        'security/category.xml',
        'security/access.xml',
        'data/company.xml',
        'data/user.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
