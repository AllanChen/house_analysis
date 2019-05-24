import pymysql

class Dbhelper:
	def __init__(self):
		self.connect = pymysql.connect(
			host='localhost',
			db='spider',
			user='root',
			passwd='root',
			charset='utf8',
			use_unicode=True)
	
	def excute_mysql_action(self):
		try:
			# with self.connect.cursor() as cursor:
			#     # Create a new record
			#     sql = "INSERT INTO `hours` (`title`) VALUES (%s)"
			#     cursor.execute(sql, ('webmaster@python.org'))
			#
			# self.connect.commit()
			
			with self.connect.cursor() as cursor:
				# Read a single record
				sql = "SELECT * FROM `hours`"
				cursor.execute(sql)
				result = cursor.fetchall()
				print(result)
		finally:
			self.connect.close()
	
	def insert_sql(self, sql):
		try:
			with self.connect.cursor() as cursor:
				# sql = "INSERT INTO `hours` (`title`) VALUES (%s)"
				cursor.execute(sql)
			
			self.connect.commit()
			
			# with self.connect.cursor() as cursor:
			#     # Read a single record
			#     sql = "SELECT * FROM `hours`"
			#     cursor.execute(sql)
			#     result = cursor.fetchall()
			#     print(result)
		finally:
			self.connect.close()
