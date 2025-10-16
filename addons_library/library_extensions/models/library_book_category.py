from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(
        string="Name",
        required=True
    )
    
    # Ensure category is unique
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The category name must be unique! Please try again and choose a different name.')
    ]