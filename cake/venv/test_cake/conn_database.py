import MySQLdb
def conn_db():
    # 连接数据库
    conn = MySQLdb.connect(
        host="192.168.1.8",
        user="root",
        passwd="lcx9527",
        db="cake",
        port=3306,
        charset="utf8")
    # 获取数据
    '''
        cursor = conn.cursor()
    cursor.execute("select a.stock from goods a where a.name='小熊乐园';")
    #返回单条数据fetchone()，返回多条数据fetchall()
    rest = cursor.fetchone()
    # list=list(rest)
    print(rest[0])
    rest=rest[0]
    print(conn)
    print(cursor)
    cursor.close()
    conn.close()
    return rest
    '''
    return conn