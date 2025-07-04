import os
from huggingface_hub import InferenceClient

# Read error from file
with open("error.txt", "r") as f:
    error_log = f.read()

# Initialize Hugging Face client
client = InferenceClient(
    provider="together",
    api_key=os.environ["HF_TOKEN"]
)

# Send to model
completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    messages=[
        {
            "role": "user",
            "content": f"Please provide the solution for the following error:\n\n{error_log}"
        }
    ],
)

# Print AI-generated solution
print("\n--- Recommended Fix ---\n")
print(completion.choices[0].message.content)
