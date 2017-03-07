from openerp import models, fields, api, exceptions


class Marks(models.Model):
    _name = 'marks'

    student_id = fields.Many2one('students', 'Student')
    course_id = fields.Many2one('courses', 'Courses')
    exam1 = fields.Float('Exam 1')
    exam2 = fields.Float('Exam 2')
    extra = fields.Float('Discipline & Presence')
    average = fields.Float('Average Mark', compute='_get_avg_mark', store=True)
    date_exam1 = fields.Date('Date Exam1')

    # @api.one
    # @api.constrains('exam1', 'exam2', 'extra')
    # def _check_marks(self):
    #     if self.exam1 or self.exam2 or self.extra > 20:
    #         raise exceptions.ValidationError("marks must not be above 20 !!")

    @api.one
    @api.depends('exam1', 'exam2', 'extra')
    def _get_avg_mark(self):
        if self.exam1 and self.exam2 and self.extra:
            self.average = (self.exam1 + self.exam2 + self.extra) / 3
