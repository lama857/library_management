from odoo import models, fields

class Author(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
    book_ids = fields.One2many('library.book', 'author_id', string='Books')