from odoo import fields, models

class RealEstate(models.Model):
    _name = "real.estate"
    _description = "Real Estate"

    name = fields.Char()

