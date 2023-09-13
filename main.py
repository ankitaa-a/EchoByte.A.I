import win32com.client
import speech_recognition as sr
import webbrowser
import os
import openai
from config import apikey
import random

chatstr =""


def chat(query):
    global chatstr
    #print(chatstr)
    openai.api_key = apikey
    chatstr = f"\nEchoByte : "
    print("Generating\n",chatstr)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": query
            },
            {
                "role": "system",
                "content": "Hello! How can I assist you today?"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    '''
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )'''
    print(response['choices'][0]['message']['content'])
    speaker.Speak(response['choices'][0]['message']['content'])

    #chatstr += f"{response['choices'][0]['text']}\n"


    return response['choices'][0]['message']['content']


    with open(f"openai files/prompt - {random.randint(1, 787687688)}", "w") as f:
        f.write(chatstr)

    #return response['choices'][0]['text']



def ai(promp):
    openai.api_key = apikey
    text = f"OPenai response... {promp} \n*********\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=promp,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response['choices'][0]['text'])
    speaker.Speak(response['choices'][0]['text'])

    text += response['choices'][0]['text']

    if not os.path.exists("openai files"):
        os.mkdir("openai files")
    with open(f"openai files/prompt - {random.randint(1,787687688)}","w") as f:
        f.write(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = "en-in")
            print("User : ",query)
            return query
        except Exception as e:
            print("Some error occured.. Apologies from EchoByte!!")



speaker = win32com.client.Dispatch(("SAPI.SpVoice"))

'''while 1:
    print("Enter the word")
    s=input()
    speaker.Speak(s)'''

if __name__ == '__main__':
    speaker.Speak("EchoByte AI")
    while True:
        print("Listening")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],["wikipedia","https://www.wikipedia.com/"]]
        for site in sites:
            if f"OPen {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]}")
                webbrowser.open(site[1])
                break
            break

        if "open chrome".lower() in query.lower():
            speaker.Speak("opening chrome")
            os.system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
            break

        elif "exit".lower() in query.lower():
            break

        elif "using artificial intelligence".lower() in query.lower():
            ai(query)
        else:
            chat(query)


