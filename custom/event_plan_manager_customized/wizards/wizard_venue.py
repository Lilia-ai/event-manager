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
        dict2create = {
            'name': self.name,
            'street': self.stree,
            'street2': self.stree2,
            'city': self.city,
            'state_id': self.state.id,
            'zip': self.zip,
            'country_id': self.country_id.id,
            'is_venue': True
        }
        return self.env['res.partner'].sudo().create(dict2create)