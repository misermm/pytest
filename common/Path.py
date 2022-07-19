import inspect
import os
from config import conf

def project_path():
    return os.path.dirname(os.path.dirname(__file__))
    # return os.path.dirname(os.path.dirname(__file__))

def case_path():
    return "".join([project_path(), "{0}".format(conf.moudle.path)])

# def report_path():
#     return "".join([project_path(), "/report"])
#
# def result_path():
#     # return "".join([project_path(), "/result"])
#     return os.path.join(project_path(), "/result")

def config_path():
    return "".join([project_path(), "/config"])


if __name__ == '__main__':
    print(case_path())
    print(config_path())
    # print(report_path())
    print(project_path())