from collector import collect_news
from summarizer import summarize_news
from reporter import generate_html
from email_sender import send_email


def main():
    print("📰 Collecting news...")
    articles = collect_news()
    print(f"   Found {len(articles)} articles.")

    print("🤖 Analyzing with Gemini AI...")
    news_json = summarize_news(articles)

    print("📧 Generating email...")
    html = generate_html(news_json)

    print("📬 Sending email...")
    send_email(html)


if __name__ == "__main__":
    main()