# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.openacademy'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
