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
    def test_10_same_name_scription(self):
        '''
        Test create a course with same name and description
        '''
        with self.assertRaisesRegexp(
                IntegrityError,
                'new row for relation "openacademy_course" violates'
                ' check constraint "openacademy_course_name_description_check"'
                ):
            self.create_course('test', 'test', None)

    @mute_logger('openerp.sql_db')
    def test_20_two_courses_same_name(self):
        '''
        Test create two courses with same name
        '''
        self.create_course('test1', 'test_description', None)
        with self.assertRaisesRegexp(
                IntegrityError,
                'duplicate key value violates unique'
                ' constraint "openacademy_course_name_unique"'
                ):
            self.create_course('test1', 'test_description', None)

    def test_15_duplicate_course(self):
        '''
        Test to duplicate a course and check thar worlks fine
        '''
        course = self.env.ref('openacademy.course0')
        course_id = course.copy()
        print "course_id", course_id
