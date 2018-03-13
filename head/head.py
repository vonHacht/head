import sys
import os
import re

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        #else:
        #    cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]

class Head:

    __metaclass__ = Singleton

    _list = []
    _regex_headerfiles = "#include ((<[^>]+>)|(\"[^\"]+\"))"

    def __init__(self, directory_path):

        if not os.path.isdir(directory_path):
            raise Exception("This is not a valid directory path: {0}".format(directory_path))

        for sub_directories, directories, files in os.walk(directory_path):
            for file in files:
                possible_file_name = os.path.realpath(directory_path) + '/' + file
                if os.path.isfile(possible_file_name):
                    self._list.append(possible_file_name)


    def _type_of_file_(self, filename):
        return os.path.splitext(filename)[1]


    def return_all_files_within_directory(self):
        return self._list

    def return_c_files_within_directory(self):

        c_files = []

        for file in self._list:
            if self._type_of_file_(file) == '.c':
                c_files.append(file)

        return c_files

    def return_h_files_within_directory(self):

        h_files = []

        for file in self._list:
            if self._type_of_file_(file) == '.h':
                h_files.append(file)
                print(file)

        return h_files

    def return_dict_c_files_with_h_files(self):

        return_dict = {}

        for file in self.return_c_files_within_directory():

            try:
                with open(file, 'r') as io:
                    content = io.readlines()
            except IOError as e:
                raise e.message

            for line in content:
                catch = re.compile(self._regex_headerfiles).match(line)
                if catch != None:
                    return_dict[file] = catch
                else:
                    return_dict[file] = "empty"

        return return_dict