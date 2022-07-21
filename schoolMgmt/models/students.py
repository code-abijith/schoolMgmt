# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolStudents(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School Student"


    name = fields.Char(string='Name', required=True, tracking=True)
    date = fields.Datetime(string="Fee Paid On")
    parent = fields.Char(string='Parent', required=True, tracking=True)
    age = fields.Integer(string='Age',required=True, tracking=True)
    home_room_teacher = fields.Many2one('school.teacher',string='Class Teacher', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, tracking=True)
    address = fields.Text(string='Address',required=True, tracking=True)
    image = fields.Binary(string="Student Picture",required=True)
    contact_no = fields.Char(string='Contact',size=10,required=True, tracking=True)
    class_std = fields.Selection([
        ('one', '1st STD'),
        ('two', '2nd STD'),
    ],string='Standard', required=True, tracking=True)
    fees = fields.Integer(string='Fees Paid',required=True,size=4, tracking=True)
    total_fees = fields.Integer(string='Total Fee',required=True,size=4, tracking=True)
    mark_sheet = fields.Text(string="Mark Sheet",tracking=True)
    note = fields.Text(string="Note",tracking=True)



    reference = fields.Char(string='Reference_id', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('school.student') or _('New')
        return super(SchoolStudents, self).create(vals)
    # @api.multi
    # def button_print(self):
    #     print("hiiiiiiiiiiiiiii")

