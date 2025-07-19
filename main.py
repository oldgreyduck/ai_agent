import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("Error: User must enter a prompt.")
        sys.exit(1)

    user_prompt = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
        verbose = True
        print(f"User prompt: {user_prompt}")
    else:
        verbose = False

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = messages,
    )
    if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
    

if __name__ == "__main__":
    main()
