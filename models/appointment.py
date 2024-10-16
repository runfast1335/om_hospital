from odoo import models, fields, api


class HospitalAppooiment(models.Model):
    _name = "hospital.appooiment"
    _description = "hospital Appooiment"
    _inherit = "mail.thread", "mail.activity.mixin"
    _rec_name = "ref"

    patient_id = fields.Many2one("hospital.patient", string="Patient",)
    gender = fields.Selection(related="patient_id.gender",) #readonly=False
    appooiment_time = fields.Datetime(string = "appooiment time", default=fields.Date.today())
    booking_date = fields.Date(string = "booking date", default=fields.Date.today())
    ref = fields.Char(string="Refrence",readonly=True)



    @api.onchange("patient_id")
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
