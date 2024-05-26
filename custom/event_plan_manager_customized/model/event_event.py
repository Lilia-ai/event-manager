from odoo import api, fields, models

class EventFunction(models.Model):
    _inherit = 'event.event'

    def test(self):
        print('test')