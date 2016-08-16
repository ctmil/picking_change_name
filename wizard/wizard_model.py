from openerp import models, fields, api, _
from openerp.exceptions import except_orm
from openerp.osv import osv
import urllib2, httplib, urlparse, gzip, requests, json
from StringIO import StringIO
import openerp.addons.decimal_precision as dp
from datetime import date
import logging
import ast
from openerp import exceptions
from openerp.exceptions import ValidationError

#Get the logger
_logger = logging.getLogger(__name__)

class picking_change_name(models.TransientModel):
        _name = 'picking.change.name'

	name = fields.Char(string='Nuevo nombre',required=True)

	@api.multi
	def confirm_name(self):
		import pdb;pdb.set_trace()
		active_id = self.env.context['active_id']
		picking = self.env['stock.picking'].browse(active_id)
		if picking:
			vals = {
				'name': self.name
				}
			return_id = picking.write(vals)
		return None
