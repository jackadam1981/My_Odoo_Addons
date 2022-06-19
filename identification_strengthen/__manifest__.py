# -*- coding: utf-8 -*-
{
    'name': "身份证号加强",

    'summary': """
        身份证号自动计算性别，生日""",

    'description': """
        使用身份证号计算生日
            6-14位是8位的生日数字字符串
        使用身份证号计算性别
            16-17位，偶数是女性，基数是男性
    """,

    'author': "自由工作室",
    'website': "http://www.baidu.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/views.xml'

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
