from datetime import date
from odoo import models, fields


class Hospitalpatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital patient"
    _inherit = "mail.thread", "mail.activity.mixin"
    _rec_name = "name"

    # tracking=True به درد لاگ انداختن توی چتر میخوره
    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string="Date of birth")
    ref = fields.Char(string="Refrence")
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True)
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')],
                              required=True, tracking=True, default="male")
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one("hospital.appooiment",
                                     string="Appooiment")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many(comodel_name='patient.tag', string='tags')


    def _compute_age(self):
        for rec in self:
            today = date.today()
            print("today", today)
            if rec.date_of_birth:
                print("rec.date_of_birth", rec.date_of_birth, rec.date_of_birth.year)
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
