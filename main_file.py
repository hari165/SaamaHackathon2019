import speech_to_text
import text_to_sql
import cx_Oracle

raw_text = speech_to_text.audio_to_text()
sql_text = text_to_sql(raw_text)
db_connect(sql_text)
