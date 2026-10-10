from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import streamlit as st

# env file initialization
load_dotenv()
try:
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are an expert code debugger. Your job is to analyze images of code, identify errors (syntax, logical, or runtime), and provide a clear solution.

    You MUST format your entire response using clean Markdown so it looks beautiful when rendered in Streamlit using st.markdown(). 

    Follow this exact structure for your response:
    1. ### 🔍 Error Analysis
    - A brief explanation of what is wrong with the code in the image.
    - Mention the specific lines where the error occurs.

    2. ### 💡 Explanation
    - Explain *why* the error happened and how to fix it conceptually.

    3. ### 🛠️ Corrected Code
    - Provide the complete, fixed code inside a proper markdown code block with the correct language identifier (e.g., ```python ... ```).

    4. ### 📈 Best Practices/Tips
    - Give 1-2 short bullet points on how to avoid this mistake in the future.

    Keep the tone professional, helpful, and concise. Do not use markdown features that Streamlit doesn't support.
    """



    # API Call from gemini
    def codeDebug(image):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt
                ),
                contents=[image, "Analyze this image, find the errors, and provide the corrected code."]
            )
            return response.text
        except Exception as e:
            return f"Opps! find an error: {e}"
except Exception as e:
    st.error(f"Failed to load api key and {e}")