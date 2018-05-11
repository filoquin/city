# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
from openerp import models, fields

class res_country_state_city(models.Model):

    _description = "Country state city"
    _name = 'res.country.state.city'
    _order = 'name'
 

    code =  fields.Char('City Code', size = 5 ,help = 'The city code in max. five chars.')
    name = fields.Char('Name',size=64, required=True, select=True,help='Administrative divisions of a state.')
    state_id =  fields.Many2one('res.country.state', 'State', required=True)
    #country_id =  fields.Many2one('res.country', string = 'Country',related = "state_id.country_id")




