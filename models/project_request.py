from odoo import models, fields


class ProjectRequest(models.Model):
    _inherit = "project_request"

    hr_id = fields.Many2one(
        "hr.employee",
        default=lambda self: self.default_hr_user()
    )
    # INÍCIO - Inventário TI
    inv_ti_id = fields.Many2one(
        "hr.inventory",
        default=lambda self: self.default_hr_inv_user()
    )
    sharing = fields.Many2one(related="inv_ti_id.sharing")
    laptop = fields.Many2one(related="inv_ti_id.laptop")
    monitor = fields.Many2one(related="inv_ti_id.monitor")
    kit = fields.Many2one(related="inv_ti_id.kit")
    keyboard = fields.Many2one(related="inv_ti_id.keyboard")
    mouse = fields.Many2one(related="inv_ti_id.mouse")
    tel_headset = fields.Many2one(related="inv_ti_id.tel_headset")
    remote_access = fields.Many2one(related="inv_ti_id.remote_access")
    office = fields.Many2one(related="inv_ti_id.office")
    comunication = fields.Many2one(related="inv_ti_id.comunication")

    def default_hr_user(self):
        hr = self.env['hr.employee'].search([])
        for rec in hr:
            if rec.user_id.id == self.env.uid:
                return rec.id
        return

    def default_hr_inv_user(self):
        hr = self.env['hr.employee'].search([])
        hr_inv = self.env['hr.inventory'].search([])
        for rec in hr:
            if rec.user_id.id == self.env.uid:
                hr = self.env['hr.employee'].browse(rec.id)

        for rec in hr_inv:
            if rec.hr_id == hr:
                return rec.id
        return
    # FIM - Inventário TI