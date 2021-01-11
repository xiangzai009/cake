from test_cake.conn_database import *
def execute(sql):
    db=conn_db()
    cursor=db.cursor()
    cursor.execute(sql)
    rest=cursor.fetchone()
    cursor.close()
    db.close()
    return rest