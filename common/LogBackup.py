import datetime
import logging,time,os

# 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
    'notset':logging.NOTSET
}

logger = logging.getLogger()
level = 'info'


def create_file(filename):
    # Python rfind()返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回 - 1
    path = filename[0:filename.rfind('/')]
    # 判断path对象是否为一个目录
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='a', encoding='utf-8')
        fd.close()
    else:
        pass


def set_handler(levels):
    # if levels == 'error':
    #     logger.addHandler(MyLog.err_handler)
    # elif levels == 'debug':
    #     logger.addHandler(MyLog.debug_handler)
    logger.addHandler(MyLog.handler)


def remove_handler(levels):
    # if levels == 'error':
    #     logger.removeHandler(MyLog.err_handler)
    # elif levels == 'debug':
        # logger.removeHandler(MyLog.debug_handler)
    logger.removeHandler(MyLog.handler)


def get_current_time():
    # return time.strftime(MyLog.date, time.localtime(time.time()))
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


class MyLog:
    # log_meg=""
    day_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = "{}/logs/{}.log".format(path, day_time)
    # err_file = "{}/logs/{}_err.log".format(path, day_time)
    # debug_file = "{}/logs/{}_debug.log".format(path, day_time)
    logger.setLevel(LEVELS.get(level))
    create_file(log_file)
    # create_file(err_file)
    # create_file(debug_file)
    # date = '%Y-%m-%d %H:%M:%S:%f'

    handler = logging.FileHandler(log_file, encoding='utf-8')
    # err_handler = logging.FileHandler(err_file, encoding='utf-8')
    # debug_handler = logging.FileHandler(debug_file, encoding='utf-8')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + __name__ + "]" + str(log_meg))
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + __name__ +  "]" + str(log_meg))
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + str(log_meg))
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + str(log_meg))
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.critical("[CRITICAL " + get_current_time() + "]" + str(log_meg))
        remove_handler('critical')


if __name__ == "__main__":
    MyLog.debug("This is debug message")
    MyLog.info("This is info message")
    MyLog.warning("This is warning message")
    MyLog.error("This is error")
    MyLog.critical("This is critical message")
