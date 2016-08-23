# -*- coding: utf-8 -*-

from psycopg2 import IntegrityError

from openerp.tests.common import TransactionCase
from openerp.tools import mute_logger

class GlobalTestOpenAcademyCourse(TransactionCase):
    '''
    Global tests
    '''

    # Define seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to test methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    # Method of class that isn't test
    def create_course(self, course_name, course_description,
                      course_responsible_id):
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
        })
        return course_id

    # Method of test startswith 'def test_*(self):'
    @mute_logger('openerp.sql_db')
    def test_01_same_name_description(self):
        '''
        Test create a course with same name and description
        '''
        with self.assertRaisesRegexp(
                IntegrityError,
                'new row for relation "openacademy_course" violates check constraint "openacademy_course_name_description_check"'
                ):
            self.create_course('test', 'test', None)
