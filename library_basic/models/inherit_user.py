from odoo import models, fields, api


class usersInherit(models.Model):
	_inherit = 'res.users'
	
	books_ids = fields.One2many(string="Books", comodel_name="library_basic.excredit", inverse_name="borrower")
