# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2010 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#              Julio Serna (julio@vauxoo.com)
#              Isaac Lopez (isaac@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields,api

class res_country_state_city(models.Model):
    _inherit = 'res.partner'


    city_id = fields.Many2one('res.country.state.city', 'City'),



    '''def fields_view_get(self, cr, user, view_id=None, view_type='form',
                        context=None, toolbar=False, submenu=False):
        if (not view_id) and (view_type == 'form') and context \
            and context.get('force_email', False):
            view_id = self.pool.get('ir.model.data').get_object_reference(
                cr, user, 'base', 'res_partner_form_city_01')[1]
        res = super(res_partner, self).fields_view_get(cr, user,
            view_id, view_type, context, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            res['arch'] = self.fields_view_get_address(
                cr, user, res['arch'], context=context)
        return res'''
    @api.onchange('city_id')
    def _onchange_city_id(self):
        self.city = self.city_id.name
        self.state_id = self.city_id.state_id.id
        self.country_id = self.city_id.state_id.country_id.id

    """
    to do ver esto
    def onchange_state_city(self, cr, uid, ids, state_id, city_id, context=None):
        res = super(res_partner, self).onchange_state(cr, uid, ids, state_id, context)
        if city_id and state_id and self.pool.get('res.country.state.city').browse(cr, uid, city_id, context).state_id.id != state_id:
            if res and 'value' in res:
                res['value']['city'] = None
                res['value']['city_id'] = None
        return res
    """
