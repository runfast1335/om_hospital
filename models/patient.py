from odoo import models, fields

class Hospitalpatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital patient"
    _inherit = "mail.thread", "mail.activity.mixin"

    # tracking=True به درد لاگ انداختن توی چتر میخوره
    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Refrence", tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')], required=True, tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)