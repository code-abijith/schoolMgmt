# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School_MGMT',
    'version' : '1.0.0',
    'summary': 'School management',
    'sequence': -100,
    'description': """School management""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['mail','sale'],
    'data': ['security/ir.model.access.csv',
             'data/data.xml',
             'views/student_view.xml',
             'views/student_gender.xml',
             'views/teacher_view.xml',
             'views/class_view.xml',
             'views/subject_view.xml',
             'views/exam_view.xml',
             'views/fee_view.xml',
             'views/fine_view.xml',
             'views/mark_sheet_view.xml',


             ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'license': 'LGPL-3',
}
