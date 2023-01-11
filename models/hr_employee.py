from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    inv_ti_id = fields.One2many("hr.inventory", "hr_id", string="Funcionário Relacionado")