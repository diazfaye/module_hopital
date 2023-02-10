import string
from unicodedata import name
from odoo import models, fields, api


class Medicament(models.Model):
    _name = "hopital.medicament"
    _description = "Un medicament"

    name = fields.Char(
        string="Code",
    )

    libelle = fields.Char(
        string="Libelle",
    )

    @api.model
    def create(self, values):
        values["name"] = (
            self.env["ir.sequence"].next_by_code("hopital.medicament") or "/"
        )
        print("create ", values)
        return super(Medicament, self).create(values)

    def write(self, values):
        print("Update", values)
        res = super(Medicament, self).write(values)
        print(res)
        return res

    def unlink(self):
        print(self)
        for record in self:
            print(record.libelle)
        return super(Medicament, self).unlink()
