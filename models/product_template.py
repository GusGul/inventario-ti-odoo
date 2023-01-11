from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ti_inventory = fields.Boolean(string="Inventário TI?")
    hard_soft = fields.Selection([('hardware', 'Hardware'),
                                  ('software', 'Software')],
                                 string="Tipo de Produto")
    category_id = fields.Many2one("ti.category", string="Categoria",
                                  domain="[('parent_id', 'ilike', hard_soft)]")
    department_id = fields.Many2one("hr.department", string="Departamento Cadastrante")
