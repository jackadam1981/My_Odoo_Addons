# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.hr.models.hr_employee import HrEmployeePrivate


class employee_to_user(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        # 用身份证号做登录名，如果输入身份证号，则自动创建用户
        if vals.get('identification_id'):
            if len(vals.get('identification_id')) == 18:

                name = vals.get('name')
                email = vals.get('identification_id')
                users = self.env['res.users'].create({
                    'name': name,
                    'email': email,
                    'login': email,
                    'lang': 'zh_CN',
                    'tz': 'Asia/Shanghai',
                    'groups_id': [(6, 0, [1])],
                })
                # 根据新创建的用户id，关联到员工。
                vals['user_id'] = users.id
                # 执行原来的创建方法，创建有关联员工的用户。
        res = super(HrEmployeePrivate, self).create(vals)
        return res
