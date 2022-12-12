# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from odoo import models, fields, api


class excreditBook(models.Model):
	_name = 'library_basic.excredit'
	
	borrower = fields.Many2one(string='Borrower', comodel_name='res.users')
	description = fields.Text()
	user_id = fields.Many2one(string='Borrower', comodel_name='res.users')
	color = fields.Integer()
	
	borrowers_count = fields.Integer(string="Jumlah Buku Yang Dipinjam", store=True, compute='_get_borrowers_count')
	books_ids = fields.Many2many(comodel_name="library_basic.library_basic", string="Borrowed Books")
	book_id = fields.Many2one(string="List Books", comodel_name="library_basic.library_basic")
	
	start_date = fields.Date(string='Start Date', default=datetime.now().strftime('%Y-%m-01'))
	end_date = fields.Date(string='End Date', store=True, compute='_get_end_date', inverse='_set_end_date')
	duration = fields.Float(string='Duration')

	def _set_end_date(self):
		for r in self:
			if not (r.start_date and r.end_date):
				continue
			r.duration = (r.end_date - r.start_date).day + 1
	
	@api.depends('start_date')
	def _get_end_date(self): 
		for r in self:
			if not (r.start_date and r.duration):
				r.end_date = r.start_date
				continue
			
			duration = timedelta(days=r.duration, seconds=-1)
			r.end_date = r.start_date + duration
	
	@api.depends('books_ids')
	def _get_borrowers_count(self):
		for r in self:
			r.borrowers_count = len(r.books_ids)
			