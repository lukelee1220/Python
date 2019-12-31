import pymysql
def connect_wxremit_db():
    return pymysql.connect(host='10.123.5.28',
                           port=3306,
                           user='root',
                           password='root1234',
                           database='db_name',
                           charset='latin1')

connect_wxremit_db()