from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TiCategory(models.Model):
    _name = "ti.category"

    name = fields.Char("Categoria")
    parent_id = fields.Many2one(
        "ti.category",
        string="Categoria Pai",
        index=True
    )
    child_ids = fields.One2many(
        "ti.category", "parent_id",
        string="Dependentes"
    )
    _parent_store = True
    _parent_name = "parent_id"
    parent_path = fields.Char(index=True)

    @api.constrains("parent_id")
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError("Erro! Você não pode criar categorias recursivas.")