import shutil
import webbrowser
import wikipedia
import sys
import os
import time
import playsound
import speech_recognition as sr 		
from gtts import gTTS
from datetime import datetime as day
from Attendance import takeAttendance
import subprocess

def speak(text):						
	tts = gTTS(text=text, lang="en")		
	filename = "abuvoice.mp3"			
	tts.save(filename)
	playsound.playsound(filename)

def wishMe():
	hour = int(day.now().hour)
	if hour>= 0 and hour<12:
		speak("a very warm Good Morning Sir")
		print("\n**** Good Morning ****\n")

	elif hour>= 12 and hour<18:
		speak("a very Good Afternoon sir")
		print("\n**** Good Afternoon ****\n")  

	else:
		speak("A very breeze Good Evening Sir")
		print("\n**** Good Evening ****\n") 
	speak("I am your Personnel Assistant")
	print("I am your Personnel Assistant")
	speak("Tokyo 1 point o")
	print("Tokyo 1.0")

def usrname():
	speak("What should i call you sir")
	try:
		username = get_audio()
		speak("Welcome Mister")
		speak(username)
	except AssertionError as e:
		username ="ABDUL"
		speak(username)
	columns = shutil.get_terminal_size().columns
	print("#######################################".center(columns))
	print("Welcome Mr.", username.center(columns))
	print("#######################################".center(columns))
	speak("How can i Help you, Sir")
	print("How can i Help you, Sir")

def get_audio():
	r = sr.Recognizer()					
	with sr.Microphone() as source: 
		audio = r.listen(source)		
		said = ""
		try:
			print("Recognizing....\n")
			said = r.recognize_google(audio, language ='en-in')
			print(f'User said: {said}\n')
		except Exception as e:
			print("Exception: Voice Not Recognized Properly" + str(e))
	return said.lower()

def note(text):
	t1 = time.localtime()
	time1 = time.strftime("%H:%M:%S", t1)
	file_name = time.ctime().replace(" ","_").replace(":","|")+"_note.txt"
	with open(file_name,"w") as f:
		f.write(text)
	subprocess.Popen(["gedit", file_name])
	
wishMe()
usrname()

while True :
	start = time.time()
	print("\n*************************************\n")
	print("Listening the audio: \n")
	
	text = get_audio()

	NOTE_STRS=["take the complaint", "write down the complaint"]
	if text in NOTE_STRS:
		speak("What is your identity number this is only for authentication")
		authen = get_audio()
		ID_NO =["45","67","233","434","091","001","879"]
		if authen in ID_NO:
			speak("what would you like me to write down in complaint box")
			note_text = get_audio()
			note(note_text)
			speak("i have made a note of that my friend")


	HELL=["Hai","hai","hi tokyo","hai tokyo how are you","hi how are you","hi tokyo how are you"]
	if text in HELL:
		print("Answering....")
		speak("Hello Berlin, how you doing? I am glad you have called me soon !")
	
	if 'wikipedia' in text:
		speak('Searching Wikipedia...')
		text = text.replace("wikipedia", "")
		results = wikipedia.summary(text, sentences = 3)
		speak("According to Wikipedia")
		print(results)
		speak(results)

	if 'open youtube' in text:
		speak("Here you go to Youtube\n")
		webbrowser.open("https://www.youtube.com")

	if 'open google' in text:
		speak("Here you go to Google\n")
		webbrowser.open("https://www.google.com")

	if 'open stackoverflow' in text:
		speak("Here you go to Stack Over flow.Happy coding")
		webbrowser.open("htpps://www.stackoverflow.com")
		
	if 'open spotify' in text:
		speak("Here you go to spotify.Enjoy the music")
		webbrowser.open("https://www.spotify.com")
	
	if "will you be my gf" in text or "will you be my valentine" in text:  
            speak("I'm not sure about, may be you should give me some time")
 
	if "how are you" in text:
            speak("I'm fine, glad you me that")
 
	if "i love you" in text:
            speak("It's hard to understand")

	if "what is the time table tokyo" in text:
		if (day.today().strftime("%A") == 'Monday'):
			print("Answering....")
			speak("network technologies, business management or placement skills, unix and unix")

		if (day.today().strftime("%A") == 'Tuesday'):
			print("Answering....")
			speak("compiler design and compiler design, distributed systems and distributed systems")

		if (day.today().strftime("%A") == 'Wednesday'):
			print("Answering....")
			speak("network technologies, business management or placement skills, unix and unix")

		if (day.today().strftime("%A") == 'Thursday'):
			print("Answering....")
			speak("compiler design and compiler design, distributed systems and distributed systems")

		if (day.today().strftime("%A") == 'Friday'):
			print("Answering....")
			speak("only business management or placement skills")
	
		if (day.today().strftime("%A") == 'Saturday'):
			print("Answering....")
			speak("No classes Today")
	
		if (day.today().strftime("%A") == 'Sunday'):
			print("Answering....")
			speak("No classes Today")

	if "is library open tokyo" in text:
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		start = '08:30:00'
		end = '20:30:00'
		if start <= current_time <= end:
			print("Answering....")
			speak("Yes it is open and can study hard")
		else:
			print("Answering....")
			speak("no its not open, and study in your respective dormitory")

	GIRLS=["who is the care taker for girls", "who is the caretaker for girls"]
	if text in GIRLS:
		print("Answering....")
		speak("P.E.T Madam and the contact number is 9 3 4 7 2 4 4 8 1 5")
	
	ALPHA=["who is the care taker for Alpha", "who is the caretaker for Alpha","who is the caretaker for alpha","who is the care taker for alpha"]
	if text in ALPHA:
		print("Answering....")
		speak("T Mahesh Babu Sir and contact number is 9 3 8 1 2 0 7 1 5 3")
	
	GAMMA=["who is the care taker for gama", "who is the caretaker for gama"]
	if text in GAMMA:
		print("Answering....")
		speak("G Venkata Sai kishore Sir and contact number is 7036125335")
	
	DELTA=["who is the care taker for Delta", "who is the caretaker for Delta","who is the care taker for delta","who is the caretaker for delta"]
	if text in DELTA:
		print("Answering....")
		speak("S RavindranathReddy Sir and contact number is 9 zero 3 2 7 8 9 8 9 zero")
	
	EXAMS=["when are the exams for 3rd year students", "when are the exams for third year students"]
	if text in EXAMS:
		print("Answering....")
		speak("According to the Trusted Sources  Mid one is on april 9 and 10 and MId 2 is on april 14 and 15 and finally End semester will be in last week of april")

	if "when are the holidays Tokyo" in text:
		print("Answering....")
		speak("According to mee seva suresh anna, after end semester you will have holidays")

	if "tokyo play music" in text:
		print("Answering....")
		playsound.playsound('/home/lovely/Documents/Mini_Project_Offical/py_Music/DripReport - Skechers (Official Music Video) Prod. OUHBOY.mp3', True)

	ATTENDANCE = ["tokyo take attendance","take the attendance","take attendance","attendance please","attendance"]
	if text in ATTENDANCE:
		print("Started the attendance\n")
		speak("Taking the attendance professor Abdul")
		speak("Students, all of you come in line one by one")
		listt=takeAttendance()
			
	THANK = ["thankyou robot","thank you robot","thankyou","thank you","thanks namaste","namaste"]
	if text in THANK:
		print("Answering....")
		speak("Ok OK OK")
		speak("Thankyou so much Berlin and come back soon for more information ")
		print("***********************************\n")
		sys.exit()
	print("\nTime taken: ")
	print(time.time()-start)
