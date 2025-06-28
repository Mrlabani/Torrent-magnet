# Magnet to .torrent Converter Bot

A Telegram bot that accepts a magnet link and replies with a .torrent file. Hosted on **Vercel** using Flask + Pyrogram.

---

## 🚀 Deploy to Vercel (Step by Step)

### 1. Install Dependencies

- Python 3.11+
- Node.js + `vercel` CLI
- `webtorrent-cli`:
```bash
npm i -g webtorrent-cli
```

---

### 2. Telegram Bot Setup

- Create a bot via [@BotFather](https://t.me/BotFather)
- Get `API_ID`, `API_HASH` from https://my.telegram.org/apps
- Fill `.env` with your credentials

---

### 3. Deploy to Vercel

```bash
vercel login
vercel --prod
```

---

### 4. Set Webhook

```bash
curl -F "url=https://your-vercel-app.vercel.app/webhook" \
     -F "secret_token=your_secret_token" \
     "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook"
```

---

### 🧲 Now you can send a magnet link and get back a .torrent file!
