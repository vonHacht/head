from logging.directory import Directory
from configparser2 import SafeConfigParser
import configparser2
import codecs

class ErrorMessages(object):

    def __init__(self):
        self.configParser = configparser2.ConfigParser()
        directory = Directory()

        propertiesFile = "error_messages.properties"

        if directory.value_with_directory_path(propertiesFile) == False:
            raise IOError("File not found: {0}".format(propertiesFile))

        #self.configParser.read(directory.value_with_directory_path(propertiesFile), encoding="UTF-8")
        self.configParser.read_file(codecs.open(directory.value_with_directory_path(propertiesFile), "r", "utf8"))
        self.__dict__ = self._dict_attribute(self.configParser)
        self._all_attribute(self.__dict__)

    def _merge_two_dicts(self, dictOne, dictTwo):
        returnDict = dictOne.copy()
        returnDict.update(dictTwo)
        return returnDict

    def _dict_attribute(self, configParser):
        dict = {}

        for section in configParser.sections():
            for key, value in configParser.items(section):
                print(key)
                dict[key] = value

        return dict

    def _all_attribute(self, dict):
        if type(dict) is dict:
            for key, value in dict:
                self.key = value


    def ErrorMessages(self, type, message):
        message = message.lower() # Read from file as lower .. ?
        #utf8dict =

        print(self.__dict__)

        if hasattr(self, '__dict__'):
            try:
                print(self.__dict__[type])
            except KeyError:
                print("KEYERROR")
                return None
            #try:

            #except KeyError
            #possibleReturnValue = self.__dict__[type]
            #if possibleReturnValue != -1:
            #    return possibleReturnValue.format(message)

        return None



