import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="together",
    api_key=os.environ.get("HF_TOKEN")
)

error_log = os.environ.get("ERROR_MESSAGE", "No error provided")

completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    messages=[
        {
            "role": "user",
            "content": f"Please fix this error:\n\n{error_log}"
        }
    ],
)

print("\n--- Suggested Fix ---\n")
print(completion.choices[0].message.content)
