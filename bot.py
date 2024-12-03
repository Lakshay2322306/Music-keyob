from telebot import TeleBot
from yt_dlp import YoutubeDL
import os
import time

# Load the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("⚠️ BOT_TOKEN environment variable is not set!")

bot = TeleBot(BOT_TOKEN)

# yt-dlp options for downloading public YouTube videos
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/tmp/%(title)s.%(ext)s',  # Save files temporarily
}

# Bot command handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎵 Welcome to the Music Bot! 🎵\nSend me the name of a song, and I'll fetch it for you!")

@bot.message_handler(func=lambda message: True)
def download_song(message):
    song_name = message.text.strip()
    bot.reply_to(message, f"🔍 Searching for '{song_name}', please wait...")
    try:
        # Download the song using yt-dlp
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            file_path = ydl.prepare_filename(info['entries'][0])

        # Send the downloaded file to the user
        with open(file_path, 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio_file)

        # Clean up the temporary file
        os.remove(file_path)
    except Exception as e:
        bot.reply_to(message, f"⚠️ An error occurred: {e}")

# Main loop for polling messages
if __name__ == "__main__":
    while True:
        try:
            print("🤖 Bot is polling for new messages...")
            bot.polling(none_stop=True, interval=3, timeout=20)
        except Exception as e:
            print(f"⚠️ Error occurred: {e}")
            time.sleep(15)  # Wait before restarting the polling
