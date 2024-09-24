from odoo import models, fields, api

class Hospitalpatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('Female', 'female')])