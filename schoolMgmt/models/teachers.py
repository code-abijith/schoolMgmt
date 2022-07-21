# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School teacher"


    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age',required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, tracking=True)
    subject = fields.Selection([
        ('maths', 'Maths'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('science', 'Science'),
        ('malayalam', 'Malayalam')
    ], required=True, tracking=True)
    subject_1 = fields.Selection([
        ('maths', 'Maths'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('science', 'Science'),
        ('malayalam', 'Malayalam')
    ], required=True, tracking=True)
    role = fields.Selection([
        ('class', 'Class Teacher'),
        ('subject', 'Subject Teacher'),
    ],string="Role", required=True, tracking=True)
    address = fields.Text(string='Address',required=True, tracking=True)
    image = fields.Binary(string="Teacher Picture",required=True)
    contact_no = fields.Char(string='Contact',size=10,required=True, tracking=True)
    class_std = fields.Selection([
        ('one', '1st STD'),
        ('two', '2nd STD'),
    ], string='Standard', tracking=True)

    reference = fields.Char(string='Reference_id', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('school.teacher') or _('New')
        return super(SchoolTeacher, self).create(vals)

