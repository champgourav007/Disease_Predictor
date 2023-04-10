import os
import requests


def ask_chatgpt(content_type, disease_name):
  url = "https://openai80.p.rapidapi.com/chat/completions"

  payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": content_type + " " + disease_name
      }
    ]
  }
  headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "4016f28790msh0a52f90c47aeecep118ffcjsn0789f5ae976d",
    "X-RapidAPI-Host": "openai80.p.rapidapi.com"
  }

  response = requests.request("POST", url, json=payload, headers=headers)
  return str((response.json())["choices"][0]["message"]["content"])