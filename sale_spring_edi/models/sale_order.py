from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Header (next to Order Date)
    edi_order_number = fields.Char('Order number', copy=False, index=True)
    edi_ship_open_date = fields.Date('Ship Open Date', copy=False)
    edi_ship_close_date = fields.Date('Ship Close Date', copy=False)

    # "Spring Systems EDI info" tab - left column
    edi_mark_for_location = fields.Char('Mark For location', copy=False)
    edi_order_message = fields.Text('Order Message', copy=False)

    # "Spring Systems EDI info" tab - right column
    edi_order_id = fields.Char('order ID', copy=False, index=True)
    edi_division = fields.Char('Division', copy=False)
    edi_department = fields.Char('Department', copy=False)
    edi_merchandise_type = fields.Char('Merchandise Type', copy=False)
    edi_currency_code = fields.Char('Currency', copy=False,
                                    help='Currency code received on the EDI order, e.g. USD')
    edi_shipping_pay_method = fields.Char('Shipping Pay Method', copy=False)
