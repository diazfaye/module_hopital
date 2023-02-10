from datetime import datetime
import string
from odoo import models, fields, api


class Medecin(models.Model):
    _name = "hopital.medecin"
    _description = "Un medecin"

    matricule = fields.Char(
        string="Matricule",
    )
    name = fields.Char(
        string="Nom",
    )
    consultation_ids = fields.One2many(
        "hopital.consultation",
        "medecin_id",
        string="Consultations",
    )

     @api.model
     def create(self, values):
         values["matricule"] = (
             self.env["ir.sequence"].next_by_code("hopital.medecin") or "/"
         )
         print(values)
         return super(Medecin, self).create(values)
