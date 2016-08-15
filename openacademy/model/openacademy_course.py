from openerp import models, fields, api

'''
This model create model of Course
'''


class Course(models.Model):
    '''
    This class create model of course
    '''
    _name = 'openacademy.course'  # Model odoo name

    name = fields.Char(string="Title", required=True)  # Field reserved
    description = fields.Text(string='Description')
