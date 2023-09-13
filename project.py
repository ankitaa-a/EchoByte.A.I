import openai11
import gradio
import win32com.client
import speech_recognition as sr

openai.api_key = "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"

messages = [{"role": "system", "content": "EchoByte"}]
speaker = win32com.client.Dispatch(("SAPI.SpVoice"))


def chat(Input):
    messages.append({"role": "user", "content": Input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    speaker.Speak(response['choices'][0]['message']['content'])
    return reply


demo = gradio.Interface(fn=chat, inputs="text", outputs="text", title="EchoByte")

demo.launch(share=True)
