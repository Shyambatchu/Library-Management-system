import mysql.connector
class db_con():
    """

    """
    def create_db_con(self, str_usr, str_paswd, str_host, str_db_name):
        """

        :return:
        """
        mysql_conn = mysql.connector.connect(user=str_usr, password=str_paswd, host=str_host, database=str_db_name,auth_plugin='mysql_native_password')
        return mysql_conn

    def execute_mysql_qry(self, mysql_conn, str_qry):
        """

        :return:
        """
        cursor = mysql_conn.cursor()
        cursor.execute(str_qry)
        data = cursor.fetchall()
        # print("Connection established to: ", data)
        # mysql_conn.close()
        return data


# db_obj=db_con()
# mysql_conn= db_obj.create_db_con('db_name','db_password','db_address','db_name')
# db_obj.execute_mysql_qry(mysql_conn,'SELECT * FROM table1.new_table where id='+usrname.get()+'and passwd='+passwd.get())
