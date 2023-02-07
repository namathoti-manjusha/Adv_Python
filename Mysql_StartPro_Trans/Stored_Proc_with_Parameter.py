import mysql.connector
from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class HclStoredpProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            mydata=('pizza',)
            self.cursor.callproc("get_cust_details",args=mydata)
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj=HclStoredpProcedure()
connect_obj.connect('localhost','root','Manjusha@17','hcl_vijayawada')
connect_obj.execute_str_procedure()
