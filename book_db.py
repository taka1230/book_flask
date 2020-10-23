import pymysql
from book_flask.tools import read_config

class Books():
    mysql_info = {
        'default': read_config()
    }  # 所有数据库的配置

    def __init__(self, dbname, config='default'):
        self.dbname = dbname
        self.config = config

    @property
    def mysql_config(self):
        mysql_info = self.mysql_info.get(self.config)  # 获取使用哪个ip的数据库
        mysql_info['db'] = self.dbname  # 添加数据库名称
        return mysql_info


class Connect_DB(Books):
    def __init__(self, dbname, config='default'):
        super().__init__(dbname, config)  # 调用父类的构造方法
        self.conn()  # 连接数据库

    def conn(self):
        try:
            self.conn = pymysql.connect(**self.mysql_config)  # 连接数据库
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)  # 按照字典格式返回

        except Exception as e:
            print('数据连接失败！')
            raise Exception('数据库连接失败！%s' % e)

    def execute_one(self, sql):  # 执行sql取一条数据
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('sql语句有误！%s' % e)
        else:
            return self.cursor.fetchone()

    def execute_many(self, sql):  # 执行sql取所有数据 或者可以通过sql语句来控制返回值
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('sql语句有误！%s' % e)
        else:
            return self.cursor.fetchall()

    def close(self):  # 关闭数据库和游标
        self.cursor.close()
        self.conn.close()
