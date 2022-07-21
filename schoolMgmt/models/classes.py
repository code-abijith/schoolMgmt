# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolClass(models.Model):
    _name = "school.class"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School class"


    class_std = fields.Char(string='Standard', required=True, tracking=True)
    home_room_teacher = fields.Many2one('school.teacher',string='Class Teacher', tracking=True)
    maths = fields.Char(string='Maths Teacher', tracking=True)
    english = fields.Char(string='English Teacher', tracking=True)
    science = fields.Char(string='Science Teacher', tracking=True)
    hindi = fields.Char(string='Hindi Teacher', tracking=True)
    malayalam = fields.Char(string='Malayalam Teacher', tracking=True)




