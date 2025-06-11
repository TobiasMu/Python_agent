# %%
import os
import sys
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# %%
from google import genai
client = genai.Client(api_key=api_key)
if len(sys.argv) < 2:
    print("No prompt provided")
    sys.exit(1)

prompt =sys.argv[1]

model = "gemini-2.0-flash-001"

resp = client.models.generate_content(model=model, contents=prompt)
print(prompt)
# %%
print(resp.text)
print("Prompt tokens:",resp.usage_metadata.prompt_token_count)
print("Response tokens:", resp.usage_metadata.candidates_token_count)
