import cx_Oracle

def db_connection(username,password):
	path = username+'/'+password+'@127.0.0.1/XE'
	con = cx_Oracle.connect(path)
	#cur = con.cursor()
	return con

def db_executor(con, sql_text):
	cur = con.cursor()
	cur.execute(sql_text)
	result = cur.fetchall()
	for row in result:
		for item in row:
			print(item, end = "\t")
		print("")
	print("--------------------------------------------------------------------------------------------")
