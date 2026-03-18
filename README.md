# Discord Daily Avatar Bot

Automatically updates your Discord bot's avatar every day with Bing's wallpaper of the day, using GitHub Actions — cuz why not.


## How It Works

1. GitHub Actions triggers the script every day at 12:05 AM UTC (tweak it for whatever you like)
2. The script fetches Bing's daily wallpaper
3. It updates the Discord bot's avatar via the Discord API


## Setup

### 1. Create a Discord Bot
1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **New Application** → give it a name → Create
3. Go to the **Bot** tab → click **Add Bot**
4. Click **Reset Token** → copy and save it (only shown once)

> You do **not** need to invite the bot to any server. This only changes the bot's own avatar.

### 2. Create a GitHub Repo
1. Go to [github.com](https://github.com) → click **New** repository
2. Name it anything (e.g. `discord-avatar-bot`)
3. Set it to **Private**
4. Initialize with a README → Create

### 3. Add Your Bot Token as a Secret
1. In your repo go to **Settings → Secrets and variables → Actions**
2. Click **New repository secret**
3. Name: `DISCORD_TOKEN`
4. Value: your bot token from Step 1

### 4. Add the Files
Add these two files to your repo:

| File | Location in repo |
|------|-----------------|
| `update_avatar.py` | root `/` |
| `daily_avatar.yml` | `.github/workflows/` |

To create the workflow folder on GitHub: click **Add file → Create new file** and type `.github/workflows/daily_avatar.yml` as the filename — GitHub creates the folders automatically.

### 5. Edit `update_avatar.py`
No changes needed — the only variable (`DISCORD_TOKEN`) is pulled from your GitHub secret automatically.


## Configuration

Open `update_avatar.py` and adjust the config block at the top if needed:

| Variable | Default | Description |
|----------|---------|-------------|
| `BING_IDX` | `0` | `0` = today's image, `1` = yesterday's, up to `7` |



## Running Manually

You can trigger the workflow anytime without waiting for the schedule:
1. Go to your repo → **Actions** tab
2. Click **Update Discord Avatar Daily**
3. Click **Run workflow**



## Schedule

Runs daily at **12:05 AM UTC** (`5 0 * * *`).  
The 5 minute offset avoids GitHub Actions congestion at midnight.
