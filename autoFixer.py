import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="together",
    api_key=os.environ["HF_TOKEN"],
)


error_log = r"""
please provide the solution of the below issue

issue
---
Traceback (most recent call last):
  File "C:\Users\pradeep\Desktop\Learning\Python\ai.py", line 6, in <module>
    api_key=os.environ["HF_TOKEN"],
            ~~~~~~~~~~^^^^^^^^^^^^
  File "<frozen os>", line 716, in __getitem__
KeyError: 'HF_TOKEN'
"""

completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    messages=[
        {
            "role": "user",
            "content": error_log
        }
    ],
)

print(completion.choices[0].message.content)