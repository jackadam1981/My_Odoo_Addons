# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api


class identification_strengthen(models.Model):
    _inherit = 'hr.employee'

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", compute='_gender_pc', tracking=True)

    birthday = fields.Date('Date of Birth', groups="hr.group_hr_user", tracking=True)

    @api.depends('identification_id')
    def _gender_pc(self):
        for record in self:
            gender_check = record.identification_id[16:17]
            if (int(gender_check) % 2) == 0:
                result = 'female'
            else:
                result = 'male'
            record.gender = result

            birth_check = record.identification_id[6:14]
            birth_day = datetime.datetime.strptime(birth_check, "%Y%m%d")
            record.birthday = birth_day
