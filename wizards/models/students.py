from openerp import models, fields


class Students(models.Model):
    _name = 'students'

    name = fields.Char('Name')
    age = fields.Integer('Age')
    email = fields.Char('Email')
    number = fields.Integer('Student Number')
    mark_ids = fields.One2many('marks', 'student_id', 'Marks')
    level = fields.Char('Level')