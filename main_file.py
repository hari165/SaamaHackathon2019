import speech_utils
import text_utils
import db_utils
import cx_Oracle


try:
	username = 'system'
	password = 'password'
	conn = sql_to_results.db_connection(username, password)

	continue1=1
	while continue1!=0:
		try:
			raw_text = speech_utils.speech_to_text()
			sql_text = text_utils.text_to_sql(raw_text)
			db_utils.db_executor(conn, sql_text)
			continue1 = int(input('\n\nContinue? (Yes=1, No=0)'))
		except Exception as e1:
			print(e1.traceback())
			print("\n\nRetry")

except Exception as e:
	print(e)

finally:
	conn.close()
