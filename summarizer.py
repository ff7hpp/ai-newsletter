import re
import os
import google.generativeai as genai
from config import TOP_NEWS

def summarize_news(articles):
    # Get API key from environment variable (set as GitHub Secret)
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    text = ""
    for a in articles:
        text += f"Title: {a['title']}\nSummary: {a['summary']}\nLink: {a['link']}\n\n"

    prompt = f"""You are a tech news analyst.
Select the {TOP_NEWS} most important tech or AI news from the text below.
Return ONLY a valid JSON array, no extra text, no markdown, no explanation.
Format:
[
  {{"title": "...", "summary": "...", "link": "..."}}
]

News:
{text}
"""

    try:
        response = model.generate_content(prompt)
        content = response.text.strip()

        print("\n--- Gemini Raw Response ---")
        print(content)
        print("---------------------------\n")

        # Strip markdown fences if present
        content = content.replace("```json", "").replace("```", "").strip()

        # Extract JSON array safely
        match = re.search(r'\[.*\]', content, re.DOTALL)
        if match:
            return match.group(0)
        else:
            print("Warning: No JSON array found.")
            return "[]"

    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "[]"