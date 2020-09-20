# -*- coding: utf-8 -*-

import random
from googletrans import Translator
import os
import re
import webbrowser
import subprocess
from time import strftime
from urllib.request import urlopen

import speech_recognition as sr
from bs4 import BeautifulSoup as soup
from pyowm import OWM

import read as aana
from piano_main import launch as piano
from key import owm_api_key


def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('話してください...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='ja-JP')
        print(command + 'だと言った。\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command

def ok_cmd():
    response_file = ["かしこまりました", '了解です']
    aana.get_single_audio(random.choice(response_file))

def assistant(command):
    # play un fichier audio                       **play me a song
    # play une video mp.4
    # creer une list de lecture
    # creer un fichier texte et ecrire de dans
    # lancer une application                      **launch
    # creer / envoyer un mail                     **email + thundermail
    # recherche wikipedia                         **tell me about + wikipediaapi
    # recherche youtube                           **play me a song
    # faire correspondre les news avec le wiki ?  ??resuse tell me about ???
    # ouvrir google                               **open
    # help me                                     **help me
    # change wallpaper                            **change wallpaper

    # meteo                                       **current weather

    if 'そこまで' in command:
        aana.get_single_audio('さようなら')  # a faire
        exit()

    elif 'パソコン様' in command:
        response_file = ["かしこまりました", '了解です']
        aana.get_single_audio(random.choice(response_file))

    elif 'おはよう' in command or 'こんにちは' in command or 'こんばんは' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            aana.get_single_audio('おはようございます')
        elif 12 <= day_time < 18:
            aana.get_single_audio('こんにちは')
        else:
            aana.get_single_audio('こんばんは')

    elif 'ニュース' in command:
        try:
            news_url = "https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = soup(xml_page, "lxml")
            news_list = soup_page.findAll("item")
            for counter, news in enumerate(news_list[:3]):
                aana.get_audio(counter, news.title.text)
                # aana.get_response(file)  # stoquer les files dans une list est les lancer quand le reader est pres.
        except Exception as e:
            print(e)

    elif 'ピアノ' in command:
        piano()

    # elif 'くん' in command:
    #     reg_ex = re.search('(.*)くん', command)
    #     if reg_ex:
    #         appname = reg_ex.group(1)
    #     # aana.get_single_audio(f'{appname}のバか。')
    #     aana.get_single_audio(f'{appname}くんは男の人が好きだ陽。')

    elif 'とり' in command or '鳥' in command:
        from flappy_bird import run
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, 'config-feedforward.txt')
        run(config_path)

    # elif 'youtube' in command:

    elif 'を探す' in command:
        reg_ex = re.search('(.*)を探す', command)
        url = 'https://www.google.co.jp/'
        if reg_ex:
            subsearch = reg_ex.group(1)
            url = url + f'search?source=hp&ei=yW9cXqOsBeytmAWK06PgBg&q={subsearch}&oq={subsearch}'
            webbrowser.open(url)
            aana.get_single_audio(f'{subsearch}を探しました。')

    elif '画像' in command:
        reg_ex = re.search('(.*)画像', command)
        url = 'https://www.google.co.jp/'
        if reg_ex:
            subsearch = reg_ex.group(1)
            url = url + f'search?tbm=isch&source=hp&ei=yW9cXqOsBeytmAWK06PgBg&q={subsearch}&oq={subsearch}'
            webbrowser.open(url)
            aana.get_single_audio(f'{subsearch}画像を探しました。')

    elif 'を実行する。' in command:
        reg_ex = re.search('(.*)を実行する', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname+".app"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
            print(subprocess.Popen(["open", "-n", "/Applications/"], stdout=subprocess.PIPE))
            aana.get_single_audio(f'{appname}を実行する。')

    elif '天気' in command:
        reg_ex = re.search('(.*)の天気', command)
        if reg_ex:
            city = reg_ex.group(1)
            # with urlopen(f"http://api.openweathermap.org/data/2.5/weather?q=osaka&APPID=90b96ea8e22533acce3abfe3be80c607") as url:
            #     data = json.loads(url.read().decode())
            #     print(data)
            owm = OWM(API_key=owm_api_key, language='ja')
            translator = Translator()
            tmp_city = translator.translate(city, dest='en')

            obs = owm.weather_at_place(tmp_city.text)

            w = obs.get_weather()
            k = w.get_detailed_status()
            x = w.get_temperature(unit='celsius')
            aana.get_single_audio(f'{city}の天気は{k}。最高温度は{round(x["temp_max"])}と最低温度は{round(x["temp_min"])}です。')

    elif '時間' in command:
        import datetime
        now = datetime.datetime.now()
        aana.get_single_audio(f'現在の時間は{now.hour}時{now.minute}分です。')

while True:
    assistant(myCommand())

