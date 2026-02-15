import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key="API_KEY")

print("🧪 Testing Gemini API...\n")

model = genai.GenerativeModel('gemini-flash-latest')
response = model.generate_content("Say hello!")

print("SUCCESS!")
print(f"Gemini says: {response.text}")
print("\n GEMINI WORKS!")
