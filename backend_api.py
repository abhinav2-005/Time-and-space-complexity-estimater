import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_code_with_gemini(code):
    prompt = (
        "Give only the time and space complexity of this code using Big-O notation. "
        "Format the output as:\nTime Complexity: O(...)\nSpace Complexity: O(...)\n\n"
        f"Code:\n{code}\n\n"
        "If this code is wrong, just return: 'Code is Wrong'"
    )

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error contacting Gemini API: {e}"
