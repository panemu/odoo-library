# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libraryBasic(models.Model):
    _name = 'library_basic.library_basic'
    _description = 'library_basic.library_basic'

    name = fields.Char()
    genre = fields.Char()
    author = fields.Char()
    number_of_books = fields.Float(string="Number of Books", default="1")
    description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
