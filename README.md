# 🧠 AI & Tech Weekly Newsletter

> A fully automated weekly newsletter that collects the latest tech & AI news, summarizes them using **Google Gemini AI**, and delivers a clean HTML email — every Monday, with no PC or local setup required.

---

## ✨ Features

- 📰 **Auto-collects** news from top sources (TechCrunch, The Verge, Ars Technica, BBC Tech)
- 🤖 **AI-powered summaries** using Google Gemini 1.5 Flash (free tier)
- 📧 **Sends a beautiful HTML email** directly to your inbox
- ☁️ **Runs on GitHub Actions** — no PC, no server, completely free
- ⏰ **Fully automated** — fires every Monday at 8:00 AM UTC
- 🔐 **Secure** — all credentials stored as GitHub Secrets, never in code

---

## 📸 How It Works

```
RSS Feeds → Collect Articles → Gemini AI Summarizes → HTML Email → Your Inbox
```

1. GitHub Actions triggers every Monday at 8AM UTC
2. `collector.py` scrapes the latest articles from RSS feeds
3. `summarizer.py` sends them to Gemini AI and gets back the top 5
4. `reporter.py` formats them into a clean HTML email
5. `email_sender.py` sends it via Gmail SMTP

---

## 🗂️ Project Structure

```
ai-newsletter/
├── .github/
│   └── workflows/
│       └── newsletter.yml      # GitHub Actions scheduler
├── main.py                     # Entry point
├── collector.py                # RSS feed scraper
├── summarizer.py               # Gemini AI integration
├── reporter.py                 # HTML email generator
├── email_sender.py             # Gmail SMTP sender
├── config.py                   # RSS feeds & settings
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Setup Guide

### 1. Fork or Clone this Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-newsletter.git
cd ai-newsletter
```

### 2. Get a Free Gemini API Key

1. Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Click **Create API Key**
3. Copy the key

### 3. Get a Gmail App Password

> You need this instead of your regular Gmail password.

1. Go to [myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Search for **App Passwords**
4. Generate one for **Mail** → copy the 16-character password

### 4. Add GitHub Secrets

In your repository go to **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret Name | Value |
|-------------|-------|
| `GEMINI_API_KEY` | Your Gemini API key |
| `EMAIL_ADDRESS` | Your Gmail address |
| `EMAIL_PASSWORD` | Your Gmail App Password |

### 5. Enable GitHub Actions

Go to the **Actions** tab in your repo and enable workflows if prompted.

---

## ▶️ Manual Run

You can trigger the newsletter anytime without waiting for Monday:

1. Go to **Actions** tab
2. Click **Weekly AI Newsletter**
3. Click **Run workflow** → **Run workflow**

---

## ⚙️ Configuration

Edit `config.py` to customize the newsletter:

```python
# Add or remove RSS feeds
RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://arstechnica.com/feed/",
    "https://feeds.bbci.co.uk/news/technology/rss.xml",
]

TOP_NEWS = 5      # Number of articles in each newsletter
MAX_ARTICLES = 40 # Max articles to collect before filtering
```

Edit `.github/workflows/newsletter.yml` to change the schedule:

```yaml
- cron: '0 8 * * 1'  # Every Monday at 8:00 AM UTC
```

> Use [crontab.guru](https://crontab.guru) to generate custom schedules.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| `feedparser` | RSS feed parsing |
| `google-generativeai` | Gemini AI API |
| `smtplib` | Email sending |
| GitHub Actions | Cloud scheduler |

---

## 📦 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GEMINI_API_KEY="your_key_here"
export EMAIL_ADDRESS="you@gmail.com"
export EMAIL_PASSWORD="your_app_password"

# Run
python main.py
```

---

## 🔒 Security

- No API keys or passwords are ever stored in the code
- All sensitive values are stored as **GitHub Encrypted Secrets**
- Secrets are injected at runtime as environment variables

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Author

Built by **ff7hpp** — feel free to fork, improve, and share!

> ⭐ If you found this useful, consider starring the repo!
