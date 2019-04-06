import speech_recognition as sr

def speech_to_text():
	r = sr.Recognizer()

	with sr.Microphone() as source:
	        print('Say something')
	        audio = r.listen(source)
	        print('Done')

	text = r.recognize_google(audio).lower()
	return text
