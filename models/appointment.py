from odoo import models, fields

class HospitalAppooiment(models.Model):
    _name = "hospital.appooiment"
    _description = "hospital Appooiment"
    _inherit = "mail.thread", "mail.activity.mixin"

    patient_id = fields.Many2one("hospital.patient", string="Patient",)
    appooiment_time = fields.Datetime(string = "appooiment time", default=fields.Date.today())
    booking_date = fields.Date(string = "booking date", default=fields.Date.today())
