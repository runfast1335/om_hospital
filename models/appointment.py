from PIL.Image import effect_noise

from odoo import models, fields, api


class HospitalAppooiment(models.Model):
    _name = "hospital.appooiment"
    _description = "hospital Appooiment"
    _inherit = "mail.thread", "mail.activity.mixin"
    _rec_name = "ref"

    patient_id = fields.Many2one("hospital.patient", string="Patient", )
    gender = fields.Selection(related="patient_id.gender", )  # readonly=False
    appooiment_time = fields.Datetime(string="appooiment time", default=fields.Date.today())
    booking_date = fields.Date(string="booking date", default=fields.Date.today())
    prescription = fields.Html(string="Prescription")
    ref = fields.Char(string="Refrence", readonly=True,
                      help="refrenc of pation record")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority",)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'canceled')], string="string",default='draft',required=True)
    doctor_id = fields.Many2one(comodel_name="res.users", string="Doctor")
    pharmacy_lines_ids = fields.One2many(comodel_name="appointment.pharmacy.lines",
                                         inverse_name="appointment_id", string="pharmacy lines")
    hide_sales_price = fields.Boolean(string="hide sales price")

    @api.onchange("patient_id")
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def object_button(self):
        print("testttttttttttttt sucses \n\n\n")
        return {
            'effect':{
                'fadeout': 'slow',
                'message': 'click sucssesful',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = "in_consultation"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"


    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def developer_action(self):
        print('dev dooooooooooooo \n\n\n')



class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "appointment pharmacy lines"

    product_id = fields.Many2one(comodel_name="product.product", required=True)
    price_unit = fields.Float(string="price", related="product_id.list_price")
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one(comodel_name="hospital.appooiment", string="appooiment")