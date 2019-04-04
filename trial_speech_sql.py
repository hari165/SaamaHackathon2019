# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:49:32 2019

@author: HTS
"""

#import string
import speech_recognition as sr
#import speechrecognition as sr
import cx_Oracle

con = cx_Oracle.connect('system/nokia@127.0.0.1/XE')
print(con.version)
cur = con.cursor()

r = sr.Recognizer()

exit1 = False

while exit1 == False:
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        print('Done')
    
    text = r.recognize_google(audio).lower()
    print('Initial -> ',text)
    text = text.split(' ')
    #for t in range(len(text)):
    #	if text[t].lower() == 'star':
    #		text[t] = '*'
    if 'all' in text:
        text[text.index('all')] = '*'
    if 'employee' in text:
        text[text.index('employee')] = 'emp'
    if 'equals' in text:
        text[text.index('equals')] = '='
    if 'name' in text:
        text[text.index('name')] = 'ename'
    text = ' '.join(text)
    print('Final   -> ',text)
    cur.execute(text)
    #mydata1 = cur.fetchone() #retrieve the first row
    #print(mydata1[0],mydata1[1],mydata1[2]) #Print the first column retrieved(user's name)
    all_rows = cur.fetchall()
    for row in all_rows:
    # row[0] returns the first column in the query (id), row[1] returns name column.
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
            
    exit1 = bool(input("Exit? (True/False)"))

con.close()
