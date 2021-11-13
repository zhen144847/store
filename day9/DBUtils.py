import  pymysql

host="localhost"
user="root"
pwd = "root"
database="bank"

# 针对增，删，改
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=pwd,database=database)

    cursor = con.cursor()
    cursor.execute(sql,param)

    con.commit()
    cursor.close()
    con.close()

#
def select(sql,param,mode="all",size=0):
    con = pymysql.connect(host=host,user=user,password=pwd,database=database)

    cursor = con.cursor()
    cursor.execute(sql,param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()




















