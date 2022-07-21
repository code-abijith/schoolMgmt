# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolFine(models.Model):
    _name = "school.fine"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School Fine"


    name = fields.Many2one('school.student',string='Student Name', required=True, tracking=True)
    fine = fields.Integer(string='Fine',size=2, tracking=True)
    home_room_teacher = fields.Char(string='Teacher', tracking=True)
    image = fields.Binary(string="Student Picture")
    contact_no = fields.Integer(string='Contact', tracking=True)
    parent = fields.Char(string='Parent', required=True, tracking=True)
    Class_std = fields.Selection([
        ('one', '1st STD'),
        ('two', '2nd STD'),
    ], required=True, tracking=True)


