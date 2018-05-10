import mysql.connector

cnf = {
    'user': 'root',
    'password': '1234',
    'database': 'lab',
    'host': 'localhost',
    'port': 3306,
}

cnx = mysql.connector.connect(**cnf)
try:
    cur = cnx.cursor()
    try:
        # Do queries in one transaction
        # sql = ''
        # cur.execute(sql)
        cnx.commit()
    except mysql.connector.Error:
        cnx.rollback()
    finally:
        cur.close()
finally:
    cnx.close()
