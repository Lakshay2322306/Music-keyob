from telebot import TeleBot
from yt_dlp import YoutubeDL
import os

# Load your Telegram bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("⚠️ BOT_TOKEN environment variable is not set!")

bot = TeleBot(BOT_TOKEN)

# yt-dlp options for downloading public YouTube content
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "🎵 Welcome to the Music Bot! 🎵\n"
        "Send me the name of a song, and I'll fetch it for you!"
    )

@bot.message_handler(func=lambda message: True)
def download_song(message):
    song_name = message.text.strip()
    bot.reply_to(message, f"🔍 Searching for '{song_name}', please wait...")
    try:
        # Use yt-dlp to download the audio
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            file_path = ydl.prepare_filename(info['entries'][0])

        # Send the downloaded file to the user
        with open(file_path, 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio_file)

        # Clean up the downloaded file
        os.remove(file_path)
    except Exception as e:
        bot.reply_to(message, f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    print("🤖 Bot is running...")
    bot.polling()
