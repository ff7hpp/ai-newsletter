import json
from datetime import datetime


def generate_html(news_json):
    news = json.loads(news_json)
    date = datetime.now().strftime("%B %d, %Y")

    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 650px; margin: auto; padding: 20px; color: #222;">
      <h1 style="color: #1a1a2e;">🧠 AI & Tech Weekly Brief</h1>
      <p style="color: #888;">Week of {date}</p>
      <hr style="border: 1px solid #eee;">
    """

    for n in news:
        html += f"""
      <div style="margin-bottom: 28px;">
        <h2 style="font-size: 18px; margin-bottom: 6px;">{n['title']}</h2>
        <p style="margin: 0 0 8px;">{n['summary']}</p>
        <a href="{n['link']}" style="color: #4a90e2; text-decoration: none;">Read more →</a>
      </div>
      <hr style="border: none; border-top: 1px solid #f0f0f0;">
    """

    html += """
    </body>
    </html>
    """
    return html