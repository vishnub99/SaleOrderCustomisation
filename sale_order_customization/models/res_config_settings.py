from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_order_limit = fields.Float(string='Limit')

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('sale_order_customization.sale_order_limit', self.sale_order_limit)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        with_user = self.env['ir.config_parameter'].sudo()
        sale_order_limit = with_user.get_param('sale_order_customization.sale_order_limit')
        res.update(
            sale_order_limit=sale_order_limit if sale_order_limit else False,)
        return res
