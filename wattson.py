from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('lijhvssRVhPsWvUmNGh71UcmMiI_M-71Eo2nT7W5fM7B')
service = TextToSpeechV1(authenticator=authenticator)
service.set_service_url('https://stream.watsonplatform.net/text-to-speech/api')


class MySynthesizeCallback(SynthesizeCallback):
    def __init__(self, data_path):
        SynthesizeCallback.__init__(self)
        self.file_path = data_path
        self.fd = open(self.file_path, 'wb')

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print(f'Error received: {error}')

    def on_content_type(self, content_type):
        print(f'Content type: {content_type}')

    def on_timing_information(self, timing_information):
        print(timing_information)

    def on_audio_stream(self, audio_stream):
        self.fd.write(audio_stream)

    def on_close(self):
        self.fd.close()
        print('Done synthesizing. Closing the connection')


def get_audio(text, data_path):
    my_callback = MySynthesizeCallback(data_path)
    service.synthesize_using_websocket(text,
                                       my_callback,
                                       accept='audio/mp3',
                                       voice='ja-JP_EmiV3Voice'
                                       )
    return True

