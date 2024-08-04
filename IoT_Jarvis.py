import speech_recognition as sr
import random
import os
from audioplayer import AudioPlayer as ap


recognizer = sr.Recognizer()
lights_on_directory = 'Jarvis_Audio_Files/Lights_On/'
lights_off_directory = 'Jarvis_Audio_Files/Lights_Off/'

lights_on_files = []
lights_off_files = []

for file in os.listdir(lights_on_directory):
    lights_on_files.append(lights_on_directory+file)
for file in os.listdir(lights_off_directory):
    lights_off_files.append(lights_off_directory+file)


with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    while True:
        try: 
            audio = recognizer.listen(source, phrase_time_limit=2)
            command = recognizer.recognize_google(audio).lower()
            if "lights" in command and "on" in command:
                print('lights turned on')
                random_voiceline_directory = random.choice(lights_on_files)
                ap(random_voiceline_directory).play(block=True)
            elif "lights" in command and "off" in command:
                print('lights turned off')
                random_voiceline_directory = random.choice(lights_off_files)
                ap(random_voiceline_directory).play(block=True)
        except sr.UnknownValueError or sr.RequestError: 
            pass
        
