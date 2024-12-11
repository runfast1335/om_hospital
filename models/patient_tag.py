from datetime import date
from odoo import models, fields


class PatintTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string='Color')
