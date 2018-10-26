#coding=utf8
from aip import AipSpeech
import json

appId = '14460206'
apiKey = 'YcfuPFKhR4feyBpvOD1Cjrt0'
secretKey = 'tvEDMvB5FIGTt3NFsGydi7Sr9XVpveXZ'
client = AipSpeech(appId,apiKey,secretKey)
def get_file_content(filePath):
    with open(filePath,"rb") as fp:
        return fp.read()
ide=client.asr(get_file_content('16k.pcm'),format='pcm',rate=16000)
voice_text=ide['result']
print (voice_text)