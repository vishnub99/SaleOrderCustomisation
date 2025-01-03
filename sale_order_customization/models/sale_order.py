from odoo import fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    manager_reference = fields.Char(string="Manager Reference")
    sale_order_limit = fields.Float(string="Sale Order Limit")

    is_sale_admin = fields.Boolean(string="Is Manager", compute="_check_is_sale_admin")
    auto_workflow = fields.Boolean(string="Auto Workflow")

    def _check_is_sale_admin(self):
        for rec in self:
            res_user = self.env['res.users'].search([('id', '=', self._uid)])
            if res_user.has_group('sale_order_customization.sale_sale_admin'):
                rec.is_sale_admin = True
            else:
                rec.is_sale_admin = False

    def action_confirm(self):
        for rec in self:
            sale_limit = float(self.env['ir.config_parameter'].sudo().get_param('sale_order_customization'
                                                                                '.sale_order_limit'))
            if rec.amount_total > sale_limit:
                res_user = self.env['res.users'].search([('id', '=', self._uid)])
                if res_user.has_group('sale_order_customization.sale_sale_admin'):
                    return super(SaleOrder, self).action_confirm()
                else:
                    raise ValidationError(_('Sorry you are not allowed to confirm this order.'))
            else:
                return super(SaleOrder, self).action_confirm()

