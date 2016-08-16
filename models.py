# -*- coding: utf-8 -*-
from openerp import models, api, fields, exceptions
from openerp.exceptions import ValidationError
from datetime import date

class account_invoice(models.Model):
	_inherit = "stock.picking"

	@api.multi
	def change_name_action(self):
                return {'type': 'ir.actions.act_window',
                        'name': 'Cambiar numero de remito',
                        'res_model': 'picking.change.name',
			#'res_id': wizard_id.id,
                        'view_type': 'form',
                        'view_mode': 'form',
                        'target': 'new',
                        'nodestroy': True,
                        }
