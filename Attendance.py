import cv2
import json
import subprocess
import numpy as np
import face_recognition
from datetime import datetime
import time

def markAttendance(name):
	with open('attendance.csv','r+' ) as f:
		myDataList = f.readlines()
		nameList = []
		for line in myDataList:
			entry = line.split(',')
			nameList.append(entry[0])
		if name not in nameList:
			now = datetime.now()
			today = datetime.today()
			d1 = today.strftime("%d/%m/%Y")
			dtString = now.strftime('%H:%M:%S')
			f.writelines(f'\n{name},{dtString},{d1}')		
	
def takeAttendance():
	cam = cv2.VideoCapture(0)
	users_data_file = open("sharedPreference.json","r")
	data = json.load(users_data_file)
	users_data_file.close()

	known_face_names = []
	known_face_encodings= []

	for user in data["users"]:
		known_face_names.append(user["name"])
		image = face_recognition.load_image_file(user["img_path"])
		face_encode = face_recognition.face_encodings(image)[0]
		known_face_encodings.append(face_encode)

	name=""
	face_locations = []
	face_encodings = []
	face_names = []
	process_this_frame = True

	while True:
		ret, frame = cam.read()
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
		rgb_small_frame = small_frame[:, :, ::-1]

		if process_this_frame:
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

			face_names = []
			for face_encoding in face_encodings:
			    
				matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
				name = "Unknown"

				face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
				best_match_index = np.argmin(face_distances)
				if matches[best_match_index]:
					name = known_face_names[best_match_index]

				face_names.append(name)

		process_this_frame = not process_this_frame
		for (top, right, bottom, left), name in zip(face_locations, face_names):
			top *= 4
			right *= 4
			bottom *= 4
			left *= 4

			cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
			markAttendance(name)

		cv2.imshow('Attendance Face Recognizer', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cam.release()
	cv2.destroyAllWindows()
