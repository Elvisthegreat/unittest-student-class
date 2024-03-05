import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    """adding the @classmethod decorator to a method  and passing ‘cls’ as a method parameter  
    will make it a class method which acts on the  class instead of an instance of the class."""

    @classmethod # @classmethod decorator.Just to reiterate The method logic acts on the class itself instead of class instances
    def setUpClass(cls):
        print('setUpClass')

    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')   


    def setUp(self): # using the setUp method save us code repetition of having to rewrite John Doe 
        print("setup")
        self.student = Student('John', 'Doe')

     
    def tearDown(self):
        print('tearDown')
    

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, 'john.doe@email.com')


    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_apply_extension(self):
        # extend the student end date
        print('test_apply_extension')
        old_end_date = self.student.end_date
        self.student.apply_extension(5) # date extended by 5 days

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        # create the test for  a successful request
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")


    def test_course_schedule_failed(self):
        # create the test for a failed request
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")
        

if __name__ == '__main__':
    unittest.main()