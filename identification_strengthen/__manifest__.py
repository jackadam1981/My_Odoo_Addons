# -*- coding: utf-8 -*-
{
    'name': "身份证号加强",

    'summary': """
        身份证号自动计算性别，生日，年龄""",

    'description': """
        使用身份证号计算生日
            6-14位是8位的生日数字字符串
        使用身份证号计算性别
            16-17位，偶数是女性，基数是男性
        使用身份证号计算年龄
            能算生日，就能算年龄，但是不能只是在更新身份证号的时候计算，而要每天计算。
            计算两个年龄:
                一个是按生日算的年龄，real_age
                一个只算年，当前年减出生年，calculate_age
        服务器任务时间需要自己去调一下，默认是安装模块的这个时间，想调整为夜间跑任务，只要改一下下次执行时间即可。
        
    """,

    'author': "自由工作室",
    'website': "http://www.bing.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '15.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/calculate_age_cron.xml',
        'views/hr_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
