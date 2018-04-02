import os
import sys

class Directory(object):

    def __init__(self):
        self.directory, self.filename = os.path.split(os.path.abspath(__file__))

    def return_directory_path(self):
        if hasattr(self, 'directory'):
            return self.directory
        else:
            return None

    def value_with_directory_path(self, value):
        if hasattr(self, 'directory'):
            return os.path.join(self.directory, value)
        else:
            return None

    def value_exist_in_directory(self, value):
        if hasattr(self, 'directory'):
            path = os.path.join(self.directory, value)
            if os.path.isfile(path):
                return True

        return False
