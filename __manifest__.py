{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage library books and authors',
    'category': 'Tools',
    'author': 'LAMA',
    'license': 'LGPL-3',

    'depends': ['base', 'product', 'account'],
    'data': [
    'security/ir.model.access.csv',
    'views/library_author_views.xml',
    'views/library_book_views.xml',
    'views/library_borrow_views.xml',
    'views/library_partner_views.xml',
    'views/library_member_views.xml',
    'views/membership_request_views.xml',
    'views/library_sequence.xml',
    'views/invoice_views.xml',
    'views/library_menu.xml', 
    'report/report.xml',
    'report/membership_templates.xml',
    'i18n/ar.po',  
],

    'installable': True,
    'application': True,
}

