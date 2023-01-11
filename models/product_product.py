from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    # one two manies fields
    laptop_func_id = fields.One2many("hr.inventory", "laptop", string="Funcionário")
    monitor_func_id = fields.One2many("hr.inventory", "monitor", string="Funcionário")
    kit_func_id = fields.One2many("hr.inventory", "kit", string="Funcionário")
    keyboard_func_id = fields.One2many("hr.inventory", "keyboard", string="Funcionário")
    mouse_func_id = fields.One2many("hr.inventory", "mouse", string="Funcionário")
    tel_headset_func_id = fields.One2many("hr.inventory", "tel_headset", string="Funcionário")
    remote_access_func_id = fields.One2many("hr.inventory", "remote_access", string="Funcionário")
    office_func_id = fields.One2many("hr.inventory", "office", string="Funcionário")

    category = fields.Many2one(related="product_tmpl_id.category_id", string="Categoria")
    categ_parent_id = fields.Many2one(related="category.parent_id")
    notes = fields.Html(string="Informações do Produto")
    renew = fields.Date()
    system = fields.Many2one(
        "product.product", string="Sistema Operacional",
        domain="[('category', 'ilike', 'sistema operacional'),('parent_id','=',False)]")
    processor = fields.Many2one(
        "product.product",
        domain="[('category', 'ilike', 'processador'),('parent_id','=',False)]")
    memory = fields.Many2one(
        "product.product",
        domain="[('category', 'ilike', 'ram'),('parent_id','=',False)]")
    memory_2 = fields.Many2one(
        "product.product",
        domain="[('category', 'ilike', 'ram'),('parent_id','=',False)]")
    storage = fields.Many2one(
        "product.product",
        domain="[('category', 'ilike', 'armazenamento'),('parent_id','=',False)]")
    keyboard = fields.Many2one(
        "product.product",
        domain="[('category', '=', 'Teclado'),('parent_id','=',False)]")
    mouse = fields.Many2one(
        "product.product",
        domain="[('category', '=', 'Mouse'),('parent_id','=',False)]")

    # parent / child
    parent_id = fields.Many2one(
        "product.product",
        string="Relação Pai"
    )
    child_ids = fields.One2many(
        "product.product", "parent_id",
        string="Dependentes"
    )
    _parent_store = True
    _parent_name = "parent_id"
    parent_path = fields.Char(index=True)

    @api.constrains("parent_id")
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError("Erro! Você não pode criar relações recursivas.")

    def update_childs(self):
        print(self.env.uid)
        ids = []

        for rec in self:
            if rec.system:
                ids.append(rec.system.id)
            if rec.processor:
                ids.append(rec.processor.id)
            if rec.memory:
                ids.append(rec.memory.id)
            if rec.memory_2:
                ids.append(rec.memory_2.id)
            if rec.storage:
                ids.append(rec.storage.id)
            if rec.keyboard:
                ids.append(rec.keyboard.id)
            if rec.mouse:
                ids.append(rec.mouse.id)

            if len(ids) > 0:
                for child_id in ids:
                    self.write({'child_ids':[(4, child_id, 0)]})
            else:
                pass