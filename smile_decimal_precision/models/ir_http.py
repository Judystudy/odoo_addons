# -*- coding: utf-8 -*-

from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def get_currencies(self):
        res = super(IrHttp, self).get_currencies()
        currency_ids = list(res.keys())
        for currency in self.env['res.currency'].browse(currency_ids):
            res[currency.id]['digits'][1] = currency.display_decimal_places
        return res
