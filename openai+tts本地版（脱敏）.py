import os
import json
import openai
from paddlespeech.cli.tts.infer import TTSExecutor
from pydub import AudioSegment
from pydub.playback import play

openai.api_key= "s***************"


class Res():
  def __init__(self) -> None:
    pass
  
  def send(context):
    rec = openai.Completion.create(model="text-davinci-003",prompt=context,temperature=0,max_tokens=200,top_p=1,frequency_penalty=0.0,presence_penalty=0.0,stop=["\n"])
    return rec["choices"][0]["text"]


prompt="你好呀.\nQ:  我可以问问你一些问题吗?\nA:"
print(prompt[:-3])

receive = Res.send(prompt)
print ("A:", receive)

# 只能用来问一个问题
# question = input("Q:  ")
# while question != "quit":
#   prompt = 'Q:' + question + '\nA:'
#   receive = Res.send(prompt)
#   print ("A:", receive)
#   question = input("Q:  ")
# print("thank you")

# 可以进行长篇对话
num = 1
question = input("Q:  ")
while question != "quit":
  prompt = prompt + receive + 'Q:' + question + '\nA:'
  receive = Res.send(prompt)
  tts = TTSExecutor()
  tts(text=receive, output="E:\\5 计算机类\\6 openai\\output{}.wav".format(num))
  print ("A:", receive)
  song = AudioSegment.from_wav("E:\\5 计算机类\\6 openai\\output{}.wav".format(num))
  play(song)
  num = num + 1
  question = input("Q:  ")
