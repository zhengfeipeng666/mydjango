# -*- coding: utf-8 -*-
# @Time : 2020/12/9 17:27
# @Author : wangchao
# @Email : wangchao8@tiens.com
# @File : db.py
# @Project : MyDjanog
import pymysql

class Database():
    '''获取数据库的连接和返回数据库中查询到文件'''

    def get_conn(self):
        '''获取数据库连接'''
        self.conn = pymysql.Connection(host='127.0.0.1', port=3306, user='root',
                                       passwd=123456, charset="UTF8")
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        return self.cursor, self.conn


    def get_db_data(self, sql, many=None):
        '''返回查询到的数据'''
        # self.get_data = self.config_object.get_section_data("database")
        # self.conn = pymysql.Connection(host=self.get_data[0], port=int(self.get_data[1]), user=self.get_data[2], passwd=self.get_data[3], charset="UTF8")
        # self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor, self.conn = Database.get_conn(self)
        self.cursor.execute(sql)
        if many:
            self.res_data = self.cursor.fetchmany(many)
        else:
            self.res_data = self.cursor.fetchall()
        if len(self.res_data) == 0:#取不到数据
            return None
        else:
            return self.res_data  # 返回一个字典数据


    def update_db(self, sql):
        """更新数据"""
        self.cursor, self.conn = Database.get_conn(self)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        self.conn.close()

    def del_data(self,sql):
        """删除数据"""
        self.cursor, self.conn = Database.get_conn(self)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        self.conn.close()

    def close_db_connect(self):
        '''关闭数据库游标和数据库连接'''
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()