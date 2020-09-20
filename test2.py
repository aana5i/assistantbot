from wattson import get_audio as audio
import read
from os.path import join, dirname


audio_file = join(dirname(__file__), './resources/dog3.mp3')

audio('こちらでは。', audio_file)

read.play_music(audio_file)
