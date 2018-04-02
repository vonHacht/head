import unittest
from head.head import Head
from logging.error_messages import ErrorMessages
from collections import defaultdict
import os


class TestDict(unittest.TestCase):

    _test_pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code")
    _class_instance = None

    def setUp(self):

        print "================================================="
        print "Running {0}".format(__file__)
        print "Looking for files in {0}".format(self._test_pathname)
        print "================================================="

        try:
            self._class_instance = Head(self._test_pathname)
        except Exception as E:
            print ErrorMessages.test_error(1, E.message)

        pass

    #@unittest.skip("Skipping: test_dict_h_files()")
    def test_dict_h_files(self):

        dictlist = self._class_instance.return_dictlist_c_files_with_h_files()

        #self.assertIs(dictlist, type(defaultdict))

        print("\n ======= VALUES OF DICT LIST =======\n")

        for key, list in dictlist.items():
            print ("key value: {0}".format(key))
            for counter, header in enumerate(list):
                print ("header value {0}: {1}".format(counter+1, header))
