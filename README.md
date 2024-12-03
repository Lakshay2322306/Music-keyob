
# Music Bot for Telegram

This bot allows users to search for and download music using yt-dlp. It is configured for hosting on Keybo or similar headless environments.

## Features
- Search and download music from YouTube.
- Uses cookies for authenticated access to restricted content.

## Deployment Instructions
1. **Set up the environment**:
    - Install Python 3.9+ and necessary dependencies.
    - Install Chromium and make sure it's available in the PATH for headless operations.
2. **Generate cookies.txt**:
    - Use the `--cookies-from-browser` option locally with yt-dlp to generate a cookies file.
    - Upload `cookies.txt` to the bot's hosting directory.
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the bot**:
    ```bash
    python bot.py
    ```

## Environment Variables
| Variable   | Description                       | Example                      |
|------------|-----------------------------------|------------------------------|
| `BOT_TOKEN`| Your Telegram bot token          | `123456:ABC-DEF1234ghIkl...` |

## Notes
- Ensure `cookies.txt` is kept up to date.
- Use a reliable hosting service like Keybo for a smooth experience.
