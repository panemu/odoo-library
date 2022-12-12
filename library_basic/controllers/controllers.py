# -*- coding: utf-8 -*-
# from odoo import http


# class Library-basic(http.Controller):
#     @http.route('/library_basic/library_basic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_basic/library_basic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_basic.listing', {
#             'root': '/library_basic/library_basic',
#             'objects': http.request.env['library_basic.library_basic'].search([]),
#         })

#     @http.route('/library_basic/library_basic/objects/<model("library_basic.library_basic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_basic.object', {
#             'object': obj
#         })
