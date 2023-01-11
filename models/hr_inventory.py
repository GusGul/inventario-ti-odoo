from odoo import models, fields, api


class HrInventory(models.Model):
    _name = "hr.inventory"
    _rec_name = "hr_id"

    hr_id = fields.Many2one('hr.employee', string="Funcionário")
    department_id = fields.Many2one(related="hr_id.department_id", readonly=True, string="Departamento")
    ip = fields.Char(string="IP")
    ramal = fields.Char(string="Ramal")
    net_point = fields.Char(string="Ponto de Rede")
    product_prod_id = fields.Many2one("product.product")
    # hardware
    sharing = fields.Many2one("product.product", string="Compartilhamento",
                              domain="[('category', 'ilike', 'impressora')]")
    laptop = fields.Many2one("product.product", string="Notebook",
                             domain="[('category', 'ilike', 'notebook'), ('laptop_func_id', '=', False)]")
    monitor = fields.Many2one("product.product", string="Monitor",
                              domain="[('category', 'ilike', 'monitor'), ('monitor_func_id', '=', False)]")
    kit_individual = fields.Selection([('kit', 'Kit'),
                                      ('individual', 'Individual')],
                                     string="Teclado/Mouse")
    kit = fields.Many2one("product.product", string="Kit Teclado/Mouse",
                          domain="[('category', 'ilike', 'kit'), ('kit_func_id', '=', False)]")
    keyboard = fields.Many2one(
        "product.product", string="Teclado",
        domain="[('category', '=', 'Teclado'), ('parent_id', '=', False), ('keyboard_func_id', '=', False)]")
    mouse = fields.Many2one(
        "product.product", string="Mouse",
        domain="[('category', '=', 'Mouse'), ('parent_id', '=', False), ('mouse_func_id', '=', False)]")
    tel_headset = fields.Many2one(
        "product.product", string="Telefone/Headset",
        domain="[('category', 'ilike', 'comunicação'), ('category.parent_id', '=', 'Hardware'), ('tel_headset_func_id', '=', False)]")
    # software
    remote_access = fields.Many2one(
        "product.product", string="Acesso Remoto",
        domain="[('category', 'ilike', 'acesso remoto'), ('remote_access_func_id', '=', False)]")
    office = fields.Many2one(
        "product.product", string="Office",
        domain="[('category', 'ilike', 'office'), ('office_func_id', '=', False)]")
    comunication = fields.Many2one(
        "product.product", string="Comunicação",
        domain="[('category', 'ilike', 'comunicação'), ('category.parent_id', '=', 'Software')]")
    hitec = fields.Many2one(
        "product.product", string="Hitec",
        domain="[('category', 'ilike', 'hitec')]")
    mapped_folders = fields.Many2one(
        "product.product", string="Pastas Mapeadas",
        domain="[('category', 'ilike', 'pastas mapeadas')]")