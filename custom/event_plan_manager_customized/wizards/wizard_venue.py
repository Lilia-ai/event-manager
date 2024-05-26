from odoo import api, fields, models

class AddVenue(models.TransientModel):
    _name = 'wizard.add.venue'

    name = fields.Char('Venue Name')
    stree = fields.Char('Street')
    stree2 = fields.Char('Street 2')
    city = fields.Char('City')
    state = fields.Many2one('res.country.state', 'State')
    zip = fields.Char('Zip Code')
    country_id = fields.Many2one('res.country', "Country")

    def action_confirm(self):
        print("test")