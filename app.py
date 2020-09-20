# -*- coding: utf-8 -*-
# install pyaudio.whl

import speech_recognition as sr
import webbrowser
import time
from time import ctime


class Speech:
    def __init__(self, language='ja-JP'):
        self.r = sr.Recognizer()
        self._lang = language
        self.voice = ''

    def get_micro(self, ask=''):
        with sr.Microphone() as source:
            if ask:
                print(ask)
            audio = self.r.listen(source)
            voice_data = ''
            try:
                voice_data = self.r.recognize_google(audio)
            except sr.UnknownValueError:
                print('Sorry, i did not get that')
            except sr.RequestError:
                print('Sorry, i am sleeping')
            self.voice = voice_data

    def get_response(self):
        _list = ['hello', 'what time is it']
        _result = ['Hello', f'{ctime()}']
        if self.voice in _list:
            print(_result[_list.index(self.voice)])
        if 'search' in self.voice:
            self.get_micro("what did you wan't to seach")
            print(self.voice)
            url = f'https://google.com/search?q={self.voice}'
            webbrowser.get().open(url)
            print(f'search {self.voice}')
        if 'stop' in self.voice:
            exit()

    def get_conversation(self):
        while 1:
            self.get_micro()
            print(self.get_response())


time.sleep(1)
print('Hello')
s = Speech()
s.get_conversation()
