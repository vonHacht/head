from misc.error_color import ErrorColor
from misc.error_enum import ErrorEnum


class ErrorMessages(object):  # Class type object

    _test = []
    _program = []

    @staticmethod
    def _no_reusability_check(error_type, number):

        if error_type is ErrorEnum.TEST:
            if number not in ErrorMessages._test:
                ErrorMessages._test.append(number)
            else:
                raise Exception("{0}This test error code have already been used{1}"
                                .format(ErrorColor.FAIL, ErrorColor.FAIL))

        if error_type is ErrorEnum.PROGRAM:
            if number not in ErrorMessages._program:
                ErrorMessages._program.append(number)
            else:
                raise Exception("{0}This program error code have already been used{1}".
                                format(ErrorColor.FAIL, ErrorColor.FAIL))

    @staticmethod
    def test_error(number, message):
        ErrorMessages._no_reusability_check(ErrorEnum.TEST, number)
        return "[TESTERR{0}]: {1}".format(number, message)

    @staticmethod
    def program_error(number, message):
        ErrorMessages._no_reusability_check(ErrorEnum.PROGRAM, number)
        return "[ERR{0}]: {1}".format(number, message)




