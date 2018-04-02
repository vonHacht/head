from logging.directory import Directory
import configparser2

class ErrorMessages(object):

    def __init__(self):
        self.configParser = configparser2.ConfigParser()
        directory = Directory()

        propertiesFile = "error_messages.properties"

        if directory.value_with_directory_path(propertiesFile) == False:
            raise IOError("File not found: {0}".format(propertiesFile))

        self.configParser.read(directory.value_with_directory_path(propertiesFile))

        sections = self.config_section_map(self.configParser)
        print(sections)
        #self.__dict__ = self.config_section_map(sections)

    def config_section_map(self, configParser):
        dict1 = {}

        for section in configParser.sections():
            try:
                dict1[section] = configParser.get(section, 'NotAbleToInstanceWithPath')
                if dict1[section] == -1:
                    print("skip: {0}".format(section))
            except:
                print("exception on {0}!".format(section))
                dict1[section] = None

        return dict1




