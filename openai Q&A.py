import os
import json
import openai

openai.api_key= "*****"


class Res():
  def __init__(self) -> None:
    pass
  
  def send(context):
    rec = openai.Completion.create(model="text-davinci-003",prompt=context,temperature=0,max_tokens=100,top_p=1,frequency_penalty=0.0,presence_penalty=0.0,stop=["\n"])
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
while question != "quit":
  prompt = prompt + receive + 'Q:' + question + '\nA:'
  receive = Res.send(prompt)
  prompt = prompt + receive
  print ("A:", receive)
  question = input("Q:  ")
