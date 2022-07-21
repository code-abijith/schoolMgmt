# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolMark(models.Model):
    _name = "school.mark"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School Mark"

    subject = fields.Selection([
        ('maths', 'Maths'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('science','Science'),
        ('malayalam','Malayalam')
    ], required=True, tracking=True)
    teacher = fields.Many2one('school.teacher',string='Teacher', tracking=True)
    class_std = fields.Selection([
        ('one', '1st STD'),
        ('two', '2nd STD'),
    ], required=True, tracking=True)


