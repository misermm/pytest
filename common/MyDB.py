import pymysql
from config.conf import *
from common.Log import MyLog


class DataBase():

    def __init__(self, env):
        self.log = MyLog(__name__)
        conf = DbConf(env)
        self.conn = pymysql.connect(host=conf['host'], port=conf["port"], user=conf['username'],
                                    password=conf['password'], db=conf['db_name'],
                                    charset="UTF8")
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.cur_tuple = self.conn.cursor()

    # select 封装fetchone, 返回tuple
    def select_one_tuple(self, sql):
        try:
            # self.log.info('begin:{}'.format(self.conn))
            self.cur_tuple.execute(sql)
            res = self.cur_tuple.fetchone()
            # self.log.info("执行的SQL: {0}, 查询结果：{1}".format(sql, res))
            return res
        except Exception as e:
            self.log.error('执行sql: {0}, 错误：{1}'.format(sql, e))
        finally:
            self.conn.commit()
            # if 'cur' or 'conn' in dir():
            #     self.conn_close()
            #     self.log.info('再次关闭cur,conn连接成功！')

    # select 封装fetchone
    def select_one(self, sql):
        try:
            # self.log.info('begin:{}'.format(self.conn))
            self.cur.execute(sql)
            res = self.cur.fetchone()
            self.log.info("执行的SQL: {0}, 查询结果：{1}".format(sql, res))
            return res
        except Exception as e:
            self.log.error('执行sql: {0}, 错误：{1}'.format(sql, e))
        finally:
            self.conn.commit()
            # if 'cur' or 'conn' in dir():
            #     self.conn_close()
            #     self.log.info('再次关闭cur,conn连接成功！')

        # select 封装fetchall
    def select_all(self, sql):
        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
            self.log.info("执行的SQL: {0}, 查询结果：{1}".format(sql, res))
            return res
        except Exception as e:
            self.log.error('执行select错误：{}'.format(e))
        finally:
            self.conn.commit()

        # select 封装fetchall
    def select_all_tuple(self, sql):
        try:
            self.cur_tuple.execute(sql)
            res = self.cur_tuple.fetchall()
            self.log.info("执行的SQL: {0}, 查询结果：{1}".format(sql, res))
            return res
        except Exception as e:
            self.log.error('执行select错误：{}'.format(e))
        finally:
            self.conn.commit()

    # select 封装fetchone
    def update_one(self, sql):
        try:
            res = self.cur.execute(sql)
            self.log.info("执行的SQL: {0}, 结果：{1}".format(sql, res))
        except Exception as e:
            self.conn.rollback()
            self.log.error('执行sql: {0}, 错误：{1}'.format(sql, e))
        finally:
            self.conn.commit()

    # select 封装fetchone
    def delete_one(self, sql):
        try:
            res = self.cur.execute(sql)
            self.log.info("执行的SQL: {0}, 结果：{1}".format(sql, res))
        except Exception as e:
            self.conn.rollback()
            self.log.error('执行sql: {0}, 错误：{1}'.format(sql, e))
        finally:
            self.conn.commit()


    def conn_close(self):
        self.cur.close()
        self.cur_tuple.close()
        self.conn.close()

    # def __del__(self):
    #     if self.conn or self.cur:
    #         self.conn_close()
    #         self.log.info('sql closed')


if __name__ == '__main__':
    db = DataBase(3)
    try:
        code = db.select_one('select * from cadre_plan_org_inspection where plan_id="25aa6a1804ee5d0daf73e83c7c58d00e"')
        # code = {key.lower():value for key,value in code.items()}
        # for key, value in code.items():
        #     if value == None:
        #         code[key] = "null"
        print(code)
    except Exception as e:
        print(e)
    finally:
        db.conn_close()
