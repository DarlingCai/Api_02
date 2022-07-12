"""
类方法：
get_conn(cls): 建立连接，获取连接对象
query_one(cls, sql): 查询一条数据
query_all(cls, sql): 查询全部数据
iud_data(cls, sql): 执行数据库增删改
"""

# 1.导入pymysql
import pymysql


class DBUtil(object):
    @classmethod
    def get_conn(cls):
        """建立连接，获取连接对象"""
        # 2.建立连接
        # 将形参host的内容赋值给host关键字参数
        conn = pymysql.connect(host='211.103.136.244', port=7061,
                               user='student', password='iHRM_student_2022',
                               database='ihrm', charset='utf8')

        # 3. 返回连接对象
        return conn

    @classmethod
    def query_one(cls, sql):
        """查询一条数据"""
        # 1. 获取连接对象
        conn = cls.get_conn()
        # 2. 获取游标对象
        cursor = conn.cursor()
        # 3. 执行sql语句
        cursor.execute(sql)
        # 4. 获取查询结果集的第一条数据
        one = cursor.fetchone()
        # 5. 关闭游标对象
        cursor.close()
        # 6. 关闭连接对象
        conn.close()
        # 7. 查询结果集的第一条数据
        return one

    @classmethod
    def query_all(cls, sql):
        """查询全部数据"""
        # 1. 获取连接对象
        conn = cls.get_conn()
        # 2. 获取游标对象
        cursor = conn.cursor()
        # 3. 执行sql语句
        cursor.execute(sql)
        # 4. 获取查询结果集的第一条数据
        _all = cursor.fetchall()
        # 5. 关闭游标对象
        cursor.close()
        # 6. 关闭连接对象
        conn.close()
        # 7. 查询结果集的全部数据
        return _all

    @classmethod
    def iud_data(cls, sql):
        """执行数据库增删改"""
        n = None
        # 1. 获取连接对象
        conn = cls.get_conn()
        # 2. 获取游标对象
        cursor = conn.cursor()
        try:
            # 3. 执行sql语句，返回值为影响的行数
            n = cursor.execute(sql)
        except Exception as e:
            print('e = ', e)
            # 有异常，回滚事务
            conn.rollback()
        else:
            print('没有异常，提交事务')
            # 没有异常，提交事务
            conn.commit()
        finally:
            # 关闭游标和连接对象
            print('关闭游标和连接对象')
            cursor.close()
            conn.close()

        return n


if __name__ == '__main__':
    mobile = '11122223333'  # 手机号

    # 查询一个结果
    sql = f"select * from bs_user where mobile='{mobile}'"
    one = DBUtil.query_one(sql)
    print(one)

    # 删除
    sql = f"delete from bs_user where mobile='{mobile}'"
    n = DBUtil.iud_data(sql)
    print(n)

    # 查询一个结果
    sql = f"select * from bs_user where mobile='{mobile}'"
    one = DBUtil.query_one(sql)
    print(one)
