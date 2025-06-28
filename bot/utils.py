import os
import tempfile
import subprocess
import traceback

def log_user(message):
    user = message.from_user
    print(f"[LOG] {user.id} - {user.first_name} - {message.text[:40]}")

async def convert_magnet(magnet: str):
    with tempfile.TemporaryDirectory() as tmp:
        try:
            cmd = ["webtorrent", magnet, "--out", tmp, "--quiet", "--torrent"]
            subprocess.run(cmd, check=True, timeout=60)
            for f in os.listdir(tmp):
                if f.endswith(".torrent"):
                    return os.path.join(tmp, f)
        except Exception:
            return None

def error_msg(e):
    return f"⚠️ *Error occurred:*\n```{traceback.format_exc()[:1900]}```"
