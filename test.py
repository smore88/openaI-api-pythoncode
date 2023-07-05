#!/usr/bin/env python3 
import openai
import gradio as gr
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

message_hist = []
#user_input = input("ShubhamBot>: ")

# Version 1 
# this is how you pass a single Q 
# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role":"user", "content": user_input}]
# )

# add history for the users question

# message_hist.append({"role":"user", "content": user_input})

# # this is how you build a message history for conversation
# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=message_hist
# )

# reply_content = completion["choices"][0]["message"]["content"]
# print(reply_content)

# # add history for the users question
# message_hist.append({"role":"assistant", "content": f"{reply_content}"})


# # openai.api
# #print(f' using the key: %s' % openai.api_key)

# # completion = openai.ChatCompletion.create(
# #     model="gpt-3.5-turbo",
# #     messages=[{"role":"user", "content": "how tall is he"}]
# # )
# # print(completion["choices"][0]["message"]["content"])
# print(message_hist)


# Version 2 
def chat(inp, role="user"):
    # for question in history
    message_hist.append({"role": role, "content": f"{inp}"})

    # get the answer
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_hist
    )

    # store response in history
    reply_content = completion["choices"][0]["message"]["content"]
    message_hist.append({"role":"assistant", "content": f"{reply_content}"})

    return reply_content

for i in range(2):
    user_input = input("ShubhamBot>: ")
    print(chat(user_input))
    print()


