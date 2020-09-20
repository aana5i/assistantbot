# -*- coding: utf-8 -*-
import pygame as pg
from wattson import get_audio as audio
from os.path import join, dirname, exists


def get_response(response_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 mono, 2 stereo
    buffer = 2048    # number of samples
    pg.mixer.init(freq, bitsize, channels, buffer)

    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)

    clock = pg.time.Clock()

    try:
        pg.mixer.music.load(f'./sound/{response_file}.mp3')
        print(f"{response_file} loaded!")
    except pg.error:
        print(f"File {response_file} not found! ({pg.get_error()})")
        return

    pg.mixer.music.play()

    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)


def get_audio(counter, _audio):
    for line in _audio.splitlines():
        audio_file_path = join(dirname(__file__), f'sound\\news\\news{counter}.mp3')
        if not exists(audio_file_path):
            audio(line, audio_file_path)
        get_response(f'news\\news{counter}')


def get_single_audio(text):
    audio_file_path = join(dirname(__file__), f'sound\\{text}.mp3')
    if not exists(audio_file_path):
        audio(text, audio_file_path)
    get_response(f'{text}')
