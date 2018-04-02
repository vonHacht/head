import unittest
from head.head import Head
from logging.error_messages import ErrorMessages
import os


class TestHead(unittest.TestCase):

    _test_pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code")
    _number_of_all_files = 12
    _number_of_c_files = 6
    _number_of_h_files = 5
    _class_instance = None

    def setUp(self):

        print "================================================="
        print "Looking for files in {0}".format(self._test_pathname)
        print "Expecting {0} number of all files".format(self._number_of_all_files)
        print "Expecting {0} number of c files".format(self._number_of_c_files)
        print "Expecting {0} number of h files".format(self._number_of_h_files)
        print "================================================="

        try:
            self._class_instance = Head(self._test_pathname)
        except Exception as E:
            print ErrorMessages.test_error(1, E.message)

        pass

    def test_init_exception(self):

        self.assertRaises(Exception, self._class_instance, "not a repository")
        self.assertRaises(Exception, self._class_instance, 1000)
        self.assertRaises(Exception, self._class_instance, {0, 0, 0, 0})

    #@unittest.skip("Skipping: test_return_of_files()")
    def test_return_of_files(self):

        head_instance = Head(self._test_pathname)

        self.assertNotEqual(head_instance.return_all_files_within_directory(), [])

        total_number_of_all_files = len(head_instance.return_all_files_within_directory())

        try:
            self.assertEqual(total_number_of_all_files, self._number_of_all_files)
        except Exception as e:
            self.fail(ErrorMessages.test_error(2, "Doesn't count correct amount of >all< files, i.e {0} != {1}"
                                               .format(total_number_of_all_files, self._number_of_all_files)))

        print("\n ======= ALL FILES FOUND =======\n")

        for file in head_instance.return_all_files_within_directory():
            print "{0}".format(file)

    #@unittest.skip("Skipping: test_return_of_c_files()")
    def test_return_of_c_files(self):

        head_instance = Head(self._test_pathname)

        self.assertNotEqual(head_instance.return_c_files_within_directory(), [])

        total_number_of_c_files = len(head_instance.return_c_files_within_directory())

        try:
            self.assertEqual(total_number_of_c_files, self._number_of_c_files)
        except Exception as e:
            self.fail(ErrorMessages.test_error(2, "Doesn't count correct amount of >c< files, i.e {0} != {1}"
                                               .format(total_number_of_c_files, self._number_of_c_files)))

        print("\n ======= C FILES FOUND =======\n")

        for file in head_instance.return_c_files_within_directory():
            print "{0}".format(file)

    #@unittest.skip("Skipping: test_return_of_h_files()")
    def test_return_of_h_files(self):

        head_instance = Head(self._test_pathname)

        self.assertNotEqual(head_instance.return_c_files_within_directory(), [])

        total_number_of_h_files = len(head_instance.return_h_files_within_directory())

        try:
            self.assertEqual(total_number_of_h_files, self._number_of_h_files)
        except Exception as e:
            self.fail(ErrorMessages.test_error(2, "Doesn't count correct amount of >c< files, i.e {0} != {1}"
                                               .format(total_number_of_h_files, self._number_of_h_files)))

        print("\n ======= H FILES FOUND =======\n")

        for file in head_instance.return_h_files_within_directory():
            print "{0}".format(file)
