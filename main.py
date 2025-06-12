# %%
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


load_dotenv()
api_key = os.environ.get("gemini_api_key")

# %%
if len(sys.argv) <2:
    print("there was no prompt provided")
    sys.exit(1)

prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]
# %%
client = genai.Client(api_key=api_key)
model ="gemini-2.0-flash-001"

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)


print(response.text)
if len(sys.argv)>2:
    if sys.argv[2]=="--verbose":
        print("User prompt:", prompt)
        print("Prompt tokens:",response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
