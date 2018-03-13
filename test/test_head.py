import unittest
from head.head import Head
import os
import sys


test_pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code")
number_of_all_files = 12
number_of_c_files = 6
number_of_h_files = 5

class TestHead(unittest.TestCase):

    def test_init_exception(self):

        self.assertRaises(Exception, Head, "not a repository")
        self.assertRaises(Exception, Head, 1000)
        self.assertRaises(Exception, Head, {0, 0, 0, 0})

        pass

    #@unittest.skip("Skipping: test_return_of_files()")
    def test_init_no_exception(self):

        try:
            head_instance = Head(test_pathname)
        except Exception as e:
            self.fail("test_init_no_exception failed on exception\n{0}".format(e.message))

        pass

    #@unittest.skip("Skipping: test_return_of_files()")
    def test_return_of_files(self):

        head_instance = Head(test_pathname)

        self.assertNotEqual(head_instance.return_all_files_within_directory(), [])

        total_number_of_all_files = len(head_instance.return_all_files_within_directory())

        try:
            self.assertEqual(total_number_of_all_files, number_of_all_files)
        except Exception as e:
            self.fail("Doesn't count correct amount of >all< files, i.e {0} != {1}".format(total_number_of_all_files, number_of_all_files))

        print("\n ======= ALL FILES FOUND =======\n")

        for file in head_instance.return_all_files_within_directory():
            print "{0}".format(file)

        pass

    #@unittest.skip("Skipping: test_return_of_c_files()")
    def test_return_of_c_files(self):

        head_instance = Head(test_pathname + '/code')

        self.assertNotEqual(head_instance.return_c_files_within_directory(), [])

        total_number_of_c_files = len(head_instance.return_c_files_within_directory())

        try:
            self.assertEqual(total_number_of_c_files, number_of_c_files)
        except Exception as e:
            self.fail("Doesn't count correct amount of >c< files, i.e {0} != {1}".format(total_number_of_c_files, number_of_c_files))

        print("\n ======= C FILES FOUND =======\n")

        for file in head_instance.return_c_files_within_directory():
            print "{0}".format(file)

        pass

    #@unittest.skip("Skipping: test_return_of_h_files()")
    def test_return_of_h_files(self):

        head_instance = Head(test_pathname + '/code')

        self.assertNotEqual(head_instance.return_c_files_within_directory(), [])

        total_number_of_h_files = len(head_instance.return_h_files_within_directory())

        try:
            self.assertEqual(total_number_of_h_files, number_of_h_files)
        except Exception as e:
            self.fail("Doesn't count correct amount of >h< files, i.e {0} != {1}".format(total_number_of_h_files, number_of_h_files))

        print("\n ======= H FILES FOUND =======\n")

        for file in head_instance.return_h_files_within_directory():
            print "{0}".format(file)

        pass

    @unittest.skip("Skipping: test_dict_h_files()")
    def test_dict_h_files(self):

        # TODO

        pass

if __name__ == '__main__':
    unittest.main()