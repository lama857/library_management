from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('library.author', string='Author', required=True)
    isbn = fields.Char(string='ISBN')
    publish_date = fields.Date(string='Publish Date')
    availability = fields.Boolean(string='Available', default=True)
    description = fields.Text(string='Description')