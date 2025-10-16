from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one(
        comodel_name="res.partner",
        string="Author",
        required=True
    )
    
    category_id = fields.Many2many(
        comodel_name="library.book.category",
        string="Categories"
    )