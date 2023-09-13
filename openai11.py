import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "hi\n"
        },
        {
            "role": "assistant",
            "content": "Hello! How can I assist you today?"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(response)
'''
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write an email for job"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I assist you today?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)


{
  "id": "chatcmpl-7oracIySgNUdtXH4rmf61k5x0ZNj8",
  "object": "chat.completion",
  "created": 1692356754,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Application for [Job Title] Position\n\nDear [Hiring Manager's Name],\n\nI hope this email finds you well. I am writing to express my interest in the [Job Title] position as advertised on [Job Board/Website]. With my strong background in [relevant skills/experience], I am confident that I will be a valuable asset to your team.\n\nI have [X years/months] of experience in [relevant field/industry], where I have honed my skills in [specific skills relevant to the position]. During my time at [Previous Company/Organization], I successfully [achieved specific accomplishments or projects relevant to the position]. These experiences have not only equipped me with the necessary technical skills but have also enhanced my ability to work effectively in fast-paced environments and collaborate with cross-functional teams.\n\nIn addition, I am highly proficient in [mention specific tools or software relevant to the position] and have a proven track record of [any notable achievements or certifications related to the position]. My strong attention to detail, problem-solving abilities, and effective communication skills have allowed me to consistently deliver high-quality results.\n\nI am particularly drawn to [Company Name]'s commitment to [mention company values or initiatives that resonate with you]. From my research, I have been impressed with"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 256,
    "total_tokens": 281
  }
}

{
  "id": "chatcmpl-7pIGShu5k2zLmMwGiDSWgzxcpqkxe",
  "object": "chat.completion",
  "created": 1692459292,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 22,
    "completion_tokens": 9,
    "total_tokens": 31
  }
}

'''
