import unittest
from head.head import Head
from logging.error_messages import ErrorMessages
from collections import defaultdict
import os


class TestSpecial(unittest.TestCase):

    _test_pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code")
    _class_instance = None

    def setUp(self):

        print ("=================================================")
        print ("Running {0}".format(__file__))
        print ("=================================================")

        pass

    def test_is_operator(self):

        instance_one = Head(self._test_pathname)
        instance_two = Head(self._test_pathname)

        instance_one = instance_two

        self.assertIs(instance_one, instance_two)

        pass

    def test_error_messages(self):

        errorMessages = ErrorMessages()
        #print (errorMessages.__dict__)

        pass
