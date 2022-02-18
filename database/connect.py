from sqlite3 import Cursor
import pyodbc as po

server = '192.168.146.168'
database = 'inputssp_test'
username = 'sa'
password = 'AdminSHI2016'


def connectDB():
    cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()
    return cursor


def queryData(strQuery, type):
    cursor.execute(strQuery)
    if(type == 'row'):
        row = cursor.fetchone()
    elif(type == 'all'):
        row = cursor.fetchone()
    return row


if __name__ == "__main__":
    cursor = connectDB()
    queryStr = "SELECT TOP 10 * FROM NL_Users"

    row = queryData(queryStr, 'row')
    while row:
        print(str(row[0]) + ", " + str(row[1] or '') + ", " +
              str(row[2] or '') + ", " + str(row[3] or ''))
        row = cursor.fetchone()
    cursor.close()
    del cursor
