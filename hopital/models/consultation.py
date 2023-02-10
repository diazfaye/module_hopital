from datetime import datetime
from odoo import models, fields, api


class Consultation(models.Model):
    _name = "hopital.consultation"
    _description = "Consultation"

    name = fields.Char(
        string="Numero Consultation",
        readonly=True,
    )
    date = fields.Date(string="Date Consultation")
    date_prochaine_consultation = fields.Date(string="Date Prochaine Consultation")
    patient_id = fields.Many2one(
        "hopital.patient",
        string="Patient",
    )
    medecin_id = fields.Many2one(
        "hopital.medecin",
        string="Medecin",
    )

    @api.model
    def create(self, values):
        values["name"] = (
            self.env["ir.sequence"].next_by_code("hopital.consultation") or "/"
        )
        res= super(Consultation,self).create(values)
        template = self.env.ref("hopital.email_template_consultation_patient")
        if template:
            self.env["mail.template"].browse(template.id).sudo().send_mail(
                res.id, force_send=True
            )
            self.env["mail.mail"].sudo().process_email_queue()
        return res
        