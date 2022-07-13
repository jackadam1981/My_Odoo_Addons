# -*- coding: utf-8 -*-
{
    'name': "employee_to_user",

    'summary': """
        创建员工的时候如果输入身份证号则自动创建用户，没密码，没权限，起码到IT部门的时候不用录入基本信息了，也不用返回人力资源部门链接员工和用户了。
        """,

    'description': """
        创建员工自动创建用户。
        改写hr.employee的创建方法，同步创建user，并关联
    """,

    'author': "自由工作室",
    'website': "https://jackadam.cnblogs.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden',
    'version': '15.0.0.2',
    'installable': True,
    'application': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],


}
