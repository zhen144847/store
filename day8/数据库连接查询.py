import pymysql
#连接数据库
conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='company',
            port=3306,
            charset='utf8'
)
#获取游标
cur = conn.cursor()

#执行语句
#查询出部门编号为30的所有员工
cur.execute("SELECT ename FROM t_employees WHERE deptno='30';")
print(cur.fetchall())
#所有经理的姓名、编号和部门编号
cur.execute("SELECT empno,ename,deptno FROM t_employees WHERE job='经理';")
print(cur.fetchall())
#找出奖金高于工资的员工。
cur.execute("SELECT * FROM t_employees WHERE comm > sal;")
print(cur.fetchall())
#找出奖金高于工资60%的员工。
cur.execute("SELECT * FROM t_employees WHERE (comm > sal*0.6);")
print(cur.fetchall())
#找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
cur.execute("SELECT * FROM t_employees WHERE deptno='10' AND job='经理' OR deptno=20 AND job = '分析员';")
print(cur.fetchall())
# 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
cur.execute("SELECT * FROM t_employees WHERE	deptno='10' AND job='经理' OR deptno=20 AND job = '分析员' OR job != '经理' AND job!= '武装上将' AND sal >= 3000;")
print(cur.fetchall())
# 无奖金或奖金低于1000的员工。
cur.execute("SELECT * FROM t_employees WHERE comm = NULL OR comm < 1000;")
print(cur.fetchall())
# 查询名字由三个字组成的员工。
cur.execute("SELECT * FROM t_employees WHERE CHAR_LENGTH(ename) = 3;")
print(cur.fetchall())
# 查询2000年以及以后入职的员工。
cur.execute("SELECT * FROM t_employees WHERE hiredate >= '2000-01-01';")
print(cur.fetchall())
# 查询所有员工详细信息，用编号升序排序
cur.execute("SELECT * FROM t_employees ORDER BY deptno;")
print(cur.fetchall())
# 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
cur.execute("SELECT * FROM t_employees ORDER BY sal DESC,hiredate;")
print(cur.fetchall())
# 查询每个部门的平均工资
cur.execute("SELECT b.dname,ROUND(AVG(a.sal)) AS 平均工资 FROM t_employees a,t_dept b WHERE a.deptno=b.deptno GROUP BY b.dname;")
print(cur.fetchall())
# 查询每个部门的雇员数量。
cur.execute("SELECT b.dname,COUNT(*) AS 雇员数量 FROM t_employees a,t_dept b WHERE a.deptno=b.deptno GROUP BY b.dname;")
print(cur.fetchall())
# 查询每种工作的最高工资、最低工资、人数
cur.execute("SELECT job,COUNT(job) AS 人数,MAX(sal) AS 最高工资,MIN(sal) AS 最低工资 FROM t_employees GROUP BY job;")
print(cur.fetchall())


#关闭游标
cur.close()
#关闭数据库
conn.close()
# 获取数据
# data = cur.fetchall()
# print(data)
# for i in data:
#         print(i)