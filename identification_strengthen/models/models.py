# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class identification_strengthen(models.Model):
    _inherit = 'hr.employee'

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", compute='_gender_pc', tracking=True)

    birthday = fields.Date('Date of Birth', groups="hr.group_hr_user", tracking=True)
    real_age = fields.Integer(string='真实年龄(算生日)')
    calculate_age = fields.Integer(string='简单年龄(只算年)')

    @api.depends('identification_id')
    def _gender_pc(self):
        for record in self:
            try:
                gender_check = record.identification_id[16:17]
                print(gender_check)
                if (int(gender_check) % 2) == 0:
                    result = 'female'
                else:
                    result = 'male'
                record.gender = result

                birth_check = record.identification_id[6:14]
                birth_day = datetime.datetime.strptime(birth_check, "%Y%m%d")
                record.birthday = birth_day
            except:
                record.gender = 'other'

    @api.model
    def _calculate_age(self):
        # Called by a cron
        # 计算年龄
        today_d = datetime.date.today()
        all_employee = self.search([])
        for i in all_employee:
            try:
                birth_check = str(i.identification_id)[6:14]
                birth_d = datetime.datetime.strptime(birth_check, "%Y%m%d")
                try:
                    birth_t = i.birthday.replace(year=today_d.year)
                except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
                    birth_t = i.birthday.replace(year=today_d.year, month=self.birthday.month + 1, day=1)
                finally:
                    print(today_d, birth_t)
                    print(type(today_d), type(birth_t))
                    if today_d > birth_t:
                        age = today_d.year - birth_d.year
                    else:
                        age = today_d.year - birth_d.year - 1
                    print(age)
                    i.real_age = age
                i.calculate_age = today_d.year - birth_d.year
            except:
                print('bed')
