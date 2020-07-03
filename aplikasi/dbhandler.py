import sqlite3


class DbHandler:
	def __init__(self, dbname):
		self.__dbname = dbname
		self.conn = sqlite3.connect(self.__dbname)
		self.cur  = self.conn.cursor()

	def select(self, table, select=None, where=None):
		try:
			query = ''
			if select != None:
				if type(select) == list:
					selectquery = ','.join(select)
					query 	+= f"SELECT {selectquery}"
				elif type(select) == str:
					query 	+= f"SELECT {select}"
			else:
				query 	= f"SELECT *"

			if table != None:
				tablequery = table
				query += f" FROM {table}"

			if where != None and type(where) == dict:
				keys = where.keys()
				vals = where.values()
				wherequery = []
				if len(keys) > 1 :
					for k, v in where.items():
						wherequery.append(f"{k} = '{v}'")

					wherequery = f" WHERE {' and '.join(wherequery)}"
					query += wherequery
				else:
					wherequery = f" WHERE {list(keys)[0]} = '{list(vals)[0]}'"
					query += wherequery

			result = self.cur.execute(query)

			columns 	= []
			values 		= []
			data 		= {}
			listData 	= []
			for values in result.fetchall():
				for column, value in zip(result.description, values):
					data[column[0]] = value
				listData.append(data)
				data = {}

			return listData

		except Exception as e:
			print(f"Error select {e}")
			return 0

	def insert(self, table, data):
		try:
			fields = ",".join(data.keys())
			values = []
			for v in data.values():

				if type(v) == int:
					values.append(str(v))
				else:
					values.append(f"'{v}'")
			values = ','.join(values)

			query = f"INSERT INTO {table}({fields}) VALUES({values})"
			self.cur.execute(query)
			self.conn.commit()
			if self.cur.rowcount == None:
				return 0
			else:
				return self.cur.rowcount

		except Exception as e:
			return 0
			print(f"Error insert {e}")

	def update(self, table, data, where):
		try:
			if type(data) == dict and type(where) == dict:

				# set data
				query = ''
				updateData = []
				for i, v in data.items():
					updateData.append(f"{i} = '{v}'")
				query += f"UPDATE {table} SET {', '.join(updateData)}"

				# where
				wherequery = []
				for k, v in where.items():
					wherequery.append(f"{k} = '{v}'")

				wherequery = f" WHERE {' and '.join(wherequery)}"
				query += wherequery



				self.cur.execute(query)
				self.conn.commit()

				if self.cur.rowcount == None:
					return 0
				else:
					return self.cur.rowcount

		except Exception as e:
			return 0
			print(f'update error : {e}')

	def delete(self, table, where=None):
		try:
			query = f"DELETE FROM {table}"

			if type(where) == dict:
				wherequery = []
				for i, v in where.items():
					wherequery.append(f"{i} = '{v}'")

				query += f" WHERE {' and '.join(wherequery)}"


			self.cur.execute(query)
			self.conn.commit()

			if self.cur.rowcount == None:
				return 0
			else:
				return self.cur.rowcount

		except Exception as e:
			print(f"delete error : {e}")






if __name__ == '__main__':
	dbhandler = DbHandler('mhm.db')
	print(dbhandler.select('users'))
	# print(dbhandler.select('users'))
	# print(dbhandler.delete('users', where={'username' : 'aaaa'}))
	# print(dbhandler.select('users'))
	# columns = dbhandler.cur.execute("select * from users")
	# print(columns)
	# column = []
	# for col in columns:
	# 	column.append(col[0])
	# print(column)

	# dbhandler.conn.commit()

	# data = {
	# 	'username' 	: 'sayang',
	# }
	# print(dbhandler.update('users', data, {'username' : 'aku'}))

	# dbhandler.cur.execute('DELETE FROM users')
	# dbhandler.conn.commit()
	# dbhandler.conn.close()