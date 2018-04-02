import os
import re
from collections import defaultdict
from logging.error_messages import ErrorMessages



class Head:

    # TODO: Maybe these should be instance variables and not class variables ... ?
    _list = []
    _regex_headerfiles = "#include ((<[^>]+>)|(\"[^\"]+\"))"
    _regex_headerfiles_samedirectory = "#include (\"[^\"]+\")"
    _regex_headerfiles_globaldirectory = "#include (<[^>]+>)"

    def __init__(self, directory_path):

        if not os.path.isdir(directory_path):
            raise Exception("This is not a valid directory path: {0}".format(directory_path))

        for sub_directories, directories, files in os.walk(directory_path):
            for file in files:
                possible_file_name = os.path.realpath(directory_path) + '/' + file
                if os.path.isfile(possible_file_name):
                    if possible_file_name not in self._list:
                        self._list.append(possible_file_name)

    def _type_of_file_(self, filename):
        return os.path.splitext(filename)[1]

    def _file_in_same_directory(self, file_with_path, file_to_check):
        if os.path.isfile(file_with_path):
            path, file = os.path.split(file_with_path)
            if os.path.isfile(path + '/' + file_to_check):
                return True

        return False

    def _file_in_regex(self, string, regex):

        catch = re.compile(regex).match(string)

        if catch is not None:
            filename = catch.group(1)
            return filename.strip("\"").strip("<").strip(">")
        else:
            return None

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

    def return_dictlist_c_files_with_h_files(self):

        return_dictlist = defaultdict(list)

        for file in self.return_c_files_within_directory():

            try:
                with open(file, 'r') as io:
                    content = io.readlines()
            except IOError as e:
                ErrorMessages.program_error(2, e.message)
                raise

            for line in content:
                possible_filename = self._file_in_regex(line, self._regex_headerfiles_samedirectory)
                if possible_filename is not None:
                    if self._type_of_file_(possible_filename) == '.h':
                        if self._file_in_same_directory(file, possible_filename) is True:
                            return_dictlist[file].append(possible_filename)

        return return_dictlist
