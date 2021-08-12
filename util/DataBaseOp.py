import configparser
import sys
import pymysql

class DataBaseOp:

    def __init__(self,config_file,node):
        cf = configparser.ConfigParser()
        cf.read(config_file)
        host = cf[node]['host']
        port = cf[node]['port']
        user = cf[node]['user']
        password = cf[node]['password']
        db_name = cf[node]['db']
        charset = cf[node]['charset']
        try:
           self.conn = pymysql.connect(host=host,port=port,user=user,password=password,database=db_name,charset=charset)
        except Exception as e:
            print(e)
            sys.exit()

    def select_record(self,query):
        try:
            db_cursor = self.conn.cursor()
            db_cursor.execute(query)
            query_result = db_cursor.fetchall()
            return query_result
        except Exception as e:

            db_cursor.close()
            exit()

    def create_execute(self,query):
        try:
            db_cursor = self.conn.cursor()
            db_cursor.execute(query)
            db_cursor.execute('commit')
            return True
        except Exception as e:
            db_cursor.execute('rollback')
            db_cursor.close()
            exit()

    def execute_insert(self, query, data):
        try:
            db_cursor = self.conn.cursor()
            db_cursor.execute(query, data)
            db_cursor.execute('commit')
            return True
        except Exception as e:

            db_cursor.execute('rollback')
            db_cursor.close()
            exit()

    def execute_update(self, query):
        try:
            db_cursor = self.conn.cursor()
            db_cursor.execute(query)
            db_cursor.execute('commit')
            return True
        except Exception as e:

            db_cursor.execute('rollback')
            db_cursor.close()
            exit()


    def close(self):
        self.conn.close()



