import cx_Oracle

def db_connection(username,password):
	path = username+'//'+password+'@127.0.0.1//XE'
	con = cx_Oracle(path)
	cur = con.cursor()
	return cur

def db_executor(cur, sql_text):
	cur.execute(sql_text)
	result = cur.fetchall()
	for row in result:
		for item in row:
			print(item, end = " ")
		print("")
	print("--------------------------------------------------------------------------------------------")
