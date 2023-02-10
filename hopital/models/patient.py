from datetime import datetime

from odoo import models, fields, api


class Patient(models.Model):
    _name = "hopital.patient"
    _description = "Un patient"

    @api.depends("date")
    def _compute_age(self):
        for record in self:
            if record.date:
                record.age = datetime.now().year - record.date.year
            else:
                record.age = 0

    name = fields.Char(
        string="Nom",
        required=True,
    )
    lastname = fields.Char(
        string="Prénom",
    )
    
    date = fields.Date(string="Date de Naissance")
    age = fields.Integer(string="Age", compute="_compute_age")
    email = fields.Char(
        string="Email")

    consultation_ids = fields.One2many(
        "hopital.consultation",
        "patient_id",
        string="Consultations",
    )

     # @api.model
     # def create(self, values):
     #     values["name"] = (
     #         self.env["ir.sequence"].next_by_code("hopital.patient") or "/"
     #     )
     #     print(values)
     #     return super(Patient, self).create(values)

     # @api.model
     # def default_get(self, fields):
     #     res = super(Patient, self).default_get(fields)
     #     res.update({'lastname': 'Moussa'})
     #     return res
