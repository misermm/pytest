import pytest_check as check
from common.Log import MyLog

log = MyLog(__name__)


def check_equal(expected_value, code):
    try:
        check.equal(expected_value, code)
        return True
    except:
        log.error("Assert error：expected_value is {0}, value is {1}".format(expected_value, code))


if __name__ == '__main__':
    check_equal(1, 2)
