#-*- coding:utf-8 -*-
"""
Created on 2017年12月22日

@author:zhaohuan
1、执行带参数的ＳＱＬ时，请先用sql语句指定需要输入的条件列表，然后再用tuple/list进行条件批配
２、在格式ＳＱＬ中不需要使用引号指定数据类型，系统会根据输入参数自动识别
３、在输入的值中不需要使用转意函数，系统会自动处理
"""

import pym
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
import utils.Config


class Mysql(object):
	"""
	MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现获取连接对象：conn = Mysql.getConn()
			释放连接对象;conn.close()或del conn
	"""
	#连接池对象
	__pool = None
	def __init__(self,evo):
		# 数据库构造函数，从连接池中取出连接，并生成操作游标
		self._conn = Mysql.__getConn(evo)
		self._cursor = self._conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

	@staticmethod
	def __getConn(evo):
		"""
		@summary: 静态方法，从连接池中取出连接
		@return MySQLdb.connection
		"""
		if Mysql.__pool is None:
			if evo == 'nginxlog':
				__pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20,
								  host=Config.DBHOST, port=Config.DBPORT, user=Config.DBUSER, passwd=Config.DBPWD,
								  db=Config.DBNAME_nginxlog, use_unicode=False, charset=Config.DBCHAR)
			else:
				__pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20,
								  host=Config.DBHOST, port=Config.DBPORT, user=Config.DBUSER, passwd=Config.DBPWD,
								  db=Config.DBNAME_fabulous, use_unicode=False, charset=Config.DBCHAR)
		return __pool.connection()

	def getAll(self, sql, param=None):
		"""
		@summary: 执行查询，并取出所有结果集
		@param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
		@param param: 可选参数，条件列表值（元组/列表）
		@return: result list(字典对象)/boolean 查询到的结果集
		"""
		if param is None:
			count = self._cursor.execute(sql)
		else:
			count = self._cursor.execute(sql, param)
		if count > 0:
			result = self._cursor.fetchall()
		else:
			result = False
		return result

	def getOne(self, sql, param=None):
		"""
		@summary: 执行查询，并取出第一条
		@param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
		@param param: 可选参数，条件列表值（元组/列表）
		@return: result dict 查询到的结果集
		"""
		if param is None:
			count = self._cursor.execute(sql)
		else:
			count = self._cursor.execute(sql, param)
		if count > 0:
			result = self._cursor.fetchone()
		else:
			result = False
		return result

	def getMany(self, sql, num, param=None):
		"""
		@summary: 执行查询，并取出num条结果
		@param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
		@param num:取得的结果条数
		@param param: 可选参数，条件列表值（元组/列表）
		@return: result list/boolean 查询到的结果集
		"""
		if param is None:
			count = self._cursor.execute(sql)
		else:
			count = self._cursor.execute(sql, param)
		if count > 0:
			result = self._cursor.fetchmany(num)
		else:
			result = False
		return result

	def insertOne(self, sql, value):
		"""
		@summary: 向数据表插入一条记录
		@param sql:要插入的ＳＱＬ格式
		@param value:要插入的记录数据tuple/list
		@return: insertId 受影响的行数
		"""
		self._cursor.execute(sql, value)
		print "zhixingle "
		return self.__getInsertId()

	def insertMany(self, sql, values):
		"""
		@summary: 向数据表插入多条记录
		@param sql:要插入的ＳＱＬ格式
		@param values:要插入的记录数据tuple(tuple)/list[list]
		@return: count 受影响的行数
		"""
		count = self._cursor.executemany(sql, values)
		return count

	def __getInsertId(self):
		"""
		获取当前连接最后一次插入操作生成的id,如果没有则为０
		"""
		self._cursor.execute("SELECT @@IDENTITY AS id")
		result = self._cursor.fetchall()
		print result
		return result[0]['id']

	def __query(self, sql, param=None):
		if param is None:
			count = self._cursor.execute(sql)
		else:
			count = self._cursor.execute(sql, param)
		return count

	def update(self, sql, param=None):
		"""
		@summary: 更新数据表记录
		@param sql: ＳＱＬ格式及条件，使用(%s,%s)
		@param param: 要更新的  值 tuple/list
		@return: count 受影响的行数
		"""
		return self.__query(sql, param)

	def delete(self, sql, param=None):
		"""
		@summary: 删除数据表记录
		@param sql: ＳＱＬ格式及条件，使用(%s,%s)
		@param param: 要删除的条件 值 tuple/list
		@return: count 受影响的行数
		"""
		return self.__query(sql, param)

	def begin(self):
		"""
		@summary: 开启事务
		"""
		self._conn.autocommit(0)

	def end(self, option='commit'):
		"""
		@summary: 结束事务
		"""
		if option == 'commit':
			self._conn.commit()
		else:
			self._conn.rollback()

	def dispose(self, isEnd=1):
		"""
		@summary: 释放连接池资源
		"""
		if isEnd == 1:
			self.end('commit')
		else:
			self.end('rollback');
		self._cursor.close()
		self._conn.close()



if __name__ == "__main__":
	# print Config.DBHOST, Config.DBPORT, Config.DBUSER, Config.DBPWD, Config.DBNAME, Config.DBCHAR
	mysql = Mysql('mypython')
	sql = "INSERT INTO userInfoforwpxsl(phoneNum,password,userId,accessToken,point)VALUES(%s,%s,%s,%s,%s)"
	data = ['15726816386', 'a123456', '52925', '81689e', '123']
	result = mysql.insertOne(sql, data)
	# 	print result
	if result:
		print "ok"

	mysql.dispose()
	'''
	#demo

	mysql = Mysql()

	sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
	result = mysql.getAll(sqlAll)
	if result:
		print "get all"
		for row in result:
			print "%s\t%s" % (row["uid"], row["goodsname"])
	sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
	result = mysql.getMany(sqlAll, 2)
	if result:
		print "get many"
		for row in result:
			print "%s\t%s" % (row["uid"], row["goodsname"])

	result = mysql.getOne(sqlAll)
	print "get one"
	print "%s\t%s" % (result["uid"], result["goodsname"])
	'''
