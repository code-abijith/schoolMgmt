# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolFees(models.Model):
    _name = "school.fee"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School Fee"


    name = fields.Many2one('school.student',string='Student Name', required=True, tracking=True)
    class_std = fields.Selection([
        ('one', '1st STD'),
        ('two', '2nd STD'),
    ], required=True,related='name.class_std', tracking=True)
    home_room_teacher = fields.Many2one(related='name.home_room_teacher',string='Class Teacher', tracking=True,store=True)
    image = fields.Binary(string="Student Picture",related='name.image',store=True)
    parent = fields.Char(string='Parent',related='name.parent', required=True, tracking=True)
    fees = fields.Integer(string='Fees paid',related='name.fees',required=True,size=4, tracking=True)
    total_fees = fields.Integer('Total Fee',related='name.total_fees',required=True,size=4, tracking=True)
    due = fields.Integer('Due', tracking=True)
    contact_no = fields.Char(string='Contact',related='name.contact_no', tracking=True)
    reference = fields.Char(required=True,related='name.reference', copy=False, readonly=True,
                            default=lambda self: _('New'))
    @api.onchange('fees')
    def onchange_due_change(self):
        if self.total_fees:
            self.due = self.total_fees-self.fees
