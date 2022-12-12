
from odoo import models, fields, api


class wizardBorrower(models.TransientModel):
	_name = 'library_basic.wizard_borrower'
	_description = 'library_basic.wizard_borrower'

	books_id = fields.Many2one(comodel_name="library_basic.library_basic", string="Books")
	borrower_ids = fields.Many2many(comodel_name="res.users", string="Borrowers")

	def subscribe(self):
		self.books_id.borrower_ids |= self.borrower_ids
		return{}
