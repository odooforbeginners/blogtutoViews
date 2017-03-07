from openerp import models, fields


class Courses(models.Model):
    _name = 'courses'

    name = fields.Char('Course Name')
    number = fields.Integer('Course Number')
