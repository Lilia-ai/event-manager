from odoo import api, fields, models

class IsVenuePartner(models.Model):
    _inherit = 'res.partner'

    company_type = fields.Selection(string='Company Type',
                                    selection=[('person', 'Individual'), ('company', 'Company'), ('venue', 'Venue')],
                                    compute='_compute_company_type', inverse='_write_company_type')
    is_venue = fields.Boolean(string='Is a Venue', default=False,
                                help="Check if the contact is a company, otherwise it is a person")

    @api.depends('is_company', 'is_venue')
    def _compute_company_type(self):
        for partner in self:
            type = 'person'
            if partner.is_company:
                type = 'company'
            if partner.is_venue:
                type = 'venue'

            partner.company_type = type

    def _write_company_type(self):
        for partner in self:
            dict2write = {
                'is_venue': not partner.company_type != 'venue',
                'is_company': not partner.company_type != 'company'
            }
            partner.write(dict2write)

    @api.onchange('company_type')
    def onchange_company_type(self):
        dict2write = {
            'is_venue': not self.company_type != 'venue',
            'is_company': not self.company_type != 'company'
        }
        self.write(dict2write)