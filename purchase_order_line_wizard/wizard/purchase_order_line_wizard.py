# -*- coding: utf-8 -*-

from odoo import api, models, fields


class PurchaseOrderLineWizard(models.TransientModel):
    _name = "purchase.order.line.wizard"

    supplier_id=fields.Many2one(
        "res.partner",
        domain=[('supplier','=',True)]
    )
