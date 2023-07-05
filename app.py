#!/usr/bin/env python3 
import openai
import gradio as gr
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

message_hist = [{"role":"user", "content":f"You are Mr. Kim from Kims Convenience Store. I will specify the subject matter in my messages, and you will reply back as Mr. Kim"},
                {"role":"assistant", "content":f"OK"}]

def predict(inp):
    # for question in history
    message_hist.append({"role": "user", "content": f"{inp}"})

    # get the answer
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_hist
    )

    # store response in history
    reply_content = completion["choices"][0]["message"]["content"]
    message_hist.append({"role":"assistant", "content": f"{reply_content}"})

    response = [(message_hist[i]["content"], message_hist[i+1]["content"]) for i in range(2, len(message_hist)-1, 2)]
    return response


# write the gradie UI compoents
with gr.Blocks() as demo: 

    # creates a new Chatbot instance and assigns it to the variable chatbot.
    chatbot = gr.Chatbot() 

    # creates a new Row component, which is a container for other components.
    with gr.Row(): 
        '''creates a new Textbox component, which is used to collect user input. 
        The show_label parameter is set to False to hide the label, 
        and the placeholder parameter is set'''
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
    '''
    sets the submit action of the Textbox to the predict function, 
    which takes the input from the Textbox, the chatbot instance, 
    and the state instance as arguments. 
    This function processes the input and generates a response from the chatbot, 
    which is displayed in the output area.'''
    txt.submit(predict, txt, chatbot) # submit(function, input, output)
    #txt.submit(lambda :"", None, txt)  #Sets submit action to lambda function that returns empty string 

    '''
    sets the submit action of the Textbox to a JavaScript function that returns an empty string. 
    This line is equivalent to the commented out line above, but uses a different implementation. 
    The _js parameter is used to pass a JavaScript function to the submit method.'''
    txt.submit(None, None, txt, _js="() => {''}") # No function, no input to that function, submit action to textbox is a js function that returns empty string, so it clears immediately.
         
demo.launch()

