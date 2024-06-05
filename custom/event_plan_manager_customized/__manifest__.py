{
    "name": "Event Manager Customized",
    "version": "1.0.0",
    'author': "New Programmer",
    'summary': """   Event Manager
    """,
    'description': """ 
        Module For Event planning manager.
    """,
    "sequence": 7,
    "license": "OPL-1",
    "category": "Management/Managing",
    "website": "https://www.verniy.xyz",
    "depends": ["contacts", "event_plan_manager", 'event', "sale", "website", "website_event"],
    "data": [
        "wizards/wizard_venue.xml",
        "security/ir.model.access.csv",
        
        "views/menu_access.xml",
        "views/event_form.xml",

        "data/website.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
