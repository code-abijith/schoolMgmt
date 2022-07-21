# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolExam(models.Model):
    _name = "school.exam"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School Exam"


    name = fields.Char(string='Exam Subject', required=True, tracking=True)
    teacher = fields.Char(string='Supervision Teacher', tracking=True)
    class_std = fields.Selection([
        ('one', '1st STD'),
        ('two', '2nd STD'),
    ], required=True, tracking=True)
    semester = fields.Selection([
        ('one', '1st Semester'),
        ('two', '2nd Semester')
    ], required=True, tracking=True)


