# -*- coding: utf-8 -*-
from odoo import models, fields


class EmployeeTicket(models.Model):
    _name = 'employee.ticket'
    _description = 'Employee Help Desk Ticket'
    _rec_name = 'employee_id'

    subject = fields.Char(required=True, string='Subject')
    employee_id = fields.Many2one('hr.employee', string='Name', required=True)
