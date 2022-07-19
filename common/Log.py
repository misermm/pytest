import datetime
import logging,os
from logging import handlers
import sys

# # 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG


LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
    'notset':logging.NOTSET
}

class MyLog:

    # def __init__(self, name, stream=sys.stdout):
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(LEVELS.get('info'))
        # self.day_time = datetime.datetime.now().strftime('%Y-%m-%d_%H') # %Y-%m-%d %H:%M:%S.%f
        self.day_time = datetime.datetime.now().strftime('%Y-%m-%d') # %Y-%m-%d %H:%M:%S.%f
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.log_file = "{}/logs/{}.log".format(self.path, self.day_time)
        self.handler = logging.FileHandler(self.log_file, encoding='utf-8')
        # 日志按时间分割
        # self.handler = handlers.TimedRotatingFileHandler(filename=self.log_file, when='m', interval=1,encoding='utf-8')
        # 控制台输出到日志
        # self.terminal = stream
        # self.log = open(self.log_file, 'ab', buffering=0)

    # def print(self, message):
        # self.terminal.write(str(message) + "\n")
        # self.log.write(message.encode('utf-8') + b"\n")

    # def write(self, message):
    #     # self.terminal.write(message)
    #     self.log.write(message)
    # #
    # def flush(self):
    #     # self.terminal.flush()
    #     self.log.flush()
    #
    # def isatty(self):
    #     pass
    # #
    # def close(self):
    #     self.log.close()

    def set_handler(self):
        self.logger.addHandler(self.handler)

    def remove_handler(self):
        self.logger.removeHandler(self.handler)

    def get_current_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


    def debug(self, log_meg):
        self.set_handler()
        self.logger.debug("DEBUG " + self.get_current_time() + '|' + self.name + "] " + str(log_meg))
        self.remove_handler()


    def info(self, log_meg):
        self.set_handler()
        self.logger.info("INFO [" + self.get_current_time() + '|' + self.name +  "] " + str(log_meg))
        self.remove_handler()


    def warning(self, log_meg):
       self.set_handler()
       self.logger.warning("WARNING [" + self.get_current_time() + '|' + self.name + "] " + str(log_meg))
       self.remove_handler()


    def error(self, log_meg):
        self.set_handler()
        self.logger.error("ERROR [" + self.get_current_time() + '|' + self.name + "] " + str(log_meg))
        self.remove_handler()


    def critical(self, log_meg):
        self.set_handler()
        self.logger.critical("CRITICAL [" + self.get_current_time() + '/' + self.name +  " " + str(log_meg))
        self.remove_handler()

    # def __del__(self):
    #     self.close()


if __name__ == "__main__":
    MyLog(__name__).debug("This is debug message")
    MyLog(__name__).info("This is info message")
    MyLog(__name__).warning("This is warning message")
    MyLog(__name__).error("This is error")
    MyLog(__name__).critical("This is critical message")
