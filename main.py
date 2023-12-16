from openai import OpenAI
import PySimpleGUI as sg
import openai
import requests
import OpenAI

url = "https://api.openai.com/v1/engines/gpt-3.5-turbo/completions"
headers = {
    "Authorization": "Bearer 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"
}

client = OpenAI()


def chatInput(prompt):
    openai.api_key = 'k-CX45TwM7StdI2QD3i1lWT3BlbkFJ3oJh8WmiJOpER4XvF0J8'  # Set your OpenAI API key here

    # Create a stream for chat completions
    stream = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream.iterate():
        if chunk['choices'][0]['delta']['content'] is not None:
            print(chunk['choices'][0]['delta']['content'], end="")
            return input(prompt)
 



response = requests.get(url, headers=headers)

sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()