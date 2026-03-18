import requests
import base64
import os

# ── USER CONFIG ────────────────────────────────────────────────────────────────
# DISCORD_TOKEN: no change needed here — add it as a GitHub secret
#   → repo → Settings → Secrets and variables → Actions → New repository secret
#   → Name: DISCORD_TOKEN, Value: your bot token

BING_IDX = 0  # 0 = today, 1 = yesterday, up to 7
# ──────────────────────────────────────────────────────────────────────────────

def get_bing_image():
    url = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx={BING_IDX}&n=1"
    response = requests.get(url)
    data = response.json()
    image_path = data["images"][0]["url"]
    image_url = f"https://www.bing.com{image_path}"
    image_data = requests.get(image_url).content
    return image_data

def update_discord_avatar(image_data):
    token = os.environ["DISCORD_TOKEN"]
    b64 = base64.b64encode(image_data).decode("utf-8")
    payload = {"avatar": f"data:image/jpeg;base64,{b64}"}
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}
    response = requests.patch("https://discord.com/api/v10/users/@me", json=payload, headers=headers)
    if response.status_code == 200:
        print("Avatar updated successfully!")
    else:
        print(f"Failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    image_data = get_bing_image()
    update_discord_avatar(image_data)
