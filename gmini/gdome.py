

import numpy as np

from google.api_core import retry


@retry.Retry()
def retry_chat(**kwargs):
    return genai.chat(**kwargs)


@retry.Retry()
def retry_reply(self, arg):
    return self.reply(arg)


import google.generativeai as genai

genai.configure(api_key="AIzaSyBUYLxvgWGlBn__x9-3hhme1yPmL-MKKcc")

models = [m for m in genai.list_models() if 'generateMessage' in m.supported_generation_methods]
model = models[0].name
print(model)

question = """
你叫什么名字
"""

response = retry_chat(
    model=model,
    context="You are an expert at solving word problems.",
    messages=question,
)

print(response.last)