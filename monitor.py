#!/usr/bin/env python3

#sources:

import speech_recognition as sr
from subprocess import call


#constants
with open('wit_key.txt') as fp:
    for line in fp:
        WIT_AI_KEY = line.strip()
TRIGGER_WORD = 'computer' #sphinx sucks, but is relatively accurate at not mixing up "computer" with another word


#init speech recognition
listener = sr.Recognizer()
listener.pause_threshold = 0.5 #default 0.8, but I'm impatient

#select mic & some debugging info
mic = False
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(str(i) + ': ' + name)
    if 'default' in name: #force mic choice here
        print('Using: ' + name)
        mic = sr.Microphone(device_index=i)
if not mic:
    print("Couldn't find mic, quitting.")
    quit()

#calibrate mic
with mic as source:
    print('Setting baseline, please be quiet...')
    listener.adjust_for_ambient_noise(source, duration=5)
    print('done.')

#helper to listen to mic and return audio for recognition
def listen():
    with mic:
        print('Listening...')
        audio = listener.listen(mic)
        print('done.')
        return audio

#helper to transcribe w/ wit.ai
def listen_wit():
    audio = listen()
    try:
        return listener.recognize_wit(audio, key=WIT_AI_KEY).strip()
    except sr.UnknownValueError:
        print('Wit.ai could not understand audio')
    except sr.RequestError as e:
        print('Could not request results from Wit.ai service; {0}'.format(e))
    return False

#listen with sphinx until "computer" is said, then send what comes after that to wit.ai to transcribe for command parsing
while True:
    audio = listen()
    try:
        text = listener.recognize_sphinx(audio).strip()
        print('Sphinx heard: ' + text)
        if TRIGGER_WORD in text:
            print('\a'); #terminal bell acknowledge
            text = listen_wit();
            if text == False:
                print('Quitting on error')
                quit()
            else:
                print('Wit heard: ' + text)
                if 'netflix' in text:
                    call(['google-chrome', 'https://netflix.com'])
                elif 'terminate' in text: #"quit" seems to miss too much as "what"
                    print('User requested quit')
                    quit()
    except sr.UnknownValueError:
        print('Sphinx could not understand audio')
    except sr.RequestError as e:
        print('Sphinx error; {0}'.format(e))

