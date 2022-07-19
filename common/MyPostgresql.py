import psycopg2
from common.Log import MyLog
from config.conf import *


class DataBasePostgresql():

    def __init__(self, env):
        self.log = MyLog(__name__)
        conf = DbConf(env)
        self.conn =psycopg2.connect(host=conf['host'], port=conf['port'], user=conf['username'], password=conf['password'], database=conf['db_name'])
        self.cur = self.conn.cursor()
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
            cols = [d[0] for d in self.cur.description]
            res = dict(zip(cols, res))
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
            cols = [d[0] for d in self.cur.description]
            resList = []
            for data in res:
                res = dict(zip(cols, data))
                resList.append(res)
            self.log.info("执行的SQL: {0}, 查询结果：{1}".format(sql, resList))
            return resList
        except Exception as e:
            self.log.error('执行select错误：{}'.format(e))
        finally:
            self.conn.commit()

    # select 封装fetchall
    def select_all_list(self, sql):
        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
            resList = []
            for x in res:
                for y in x:
                    resList.append(y)
            self.log.info("执行的SQL: {0}, 查询结果：{1}".format(sql, res))
            return resList
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
    db = DataBasePostgresql(6)
    try:
        # code = db.select_all_list("SELECT CODE_ITEM_ID,CODE_ITEM_NAME FROM SYS_CODE_ITEM WHERE CODE_SET_ID = '3645'")
        # orgId1 = db.select_all_list("SELECT ID FROM B001 WHERE B001005 LIKE '机构自动化%' AND B001002 !='101'")
        orgId2 = db.select_all_list("SELECT ID FROM B001 WHERE  B001002='-1' ")
        # org1 = db.select_all_list("select ID FROM C001 WHERE C001010 IN {}".format(tuple(orgId1)))
        #org2 = db.select_all_list("select ID FROM C001 WHERE C001010 IN {}".format(tuple(orgId2)))
        print(orgId2)
        #print(org2)
    except Exception as e:
        print(e)
    finally:
        db.conn_close()
