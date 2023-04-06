import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pytube
import instaloader
import spotdl
from bs4 import BeautifulSoup
import requests



def youtube_shorts(update, context):
    url = context.args[0]
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Video downloaded successfully!")

    
def insta_reels(update, context):
    url = context.args[0]
    L = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(L.context, url)
    L.download_post(post, target="#insta_reels")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Video downloaded successfully!")


def spotify(update, context):
    url = context.args[0]
    spotdl.download(url)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Song downloaded successfully!")

    
def lyrics(update, context):
    url = f"https://www.musixmatch.com/search/{context.args[0]}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    lyrics_url = soup.find("a", class_="title").get("href")
    html = requests.get(lyrics_url).text
    soup = BeautifulSoup(html, "html.parser")
    lyrics = soup.find("div", class_="mxm-lyrics__content ").text
    context.bot.send_message(chat_id=update.effective_chat.id, text=lyrics)

    
def youtube_mp3(update, context):
    url = context.args[0]
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Audio downloaded successfully!")

    
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("ytshorts", youtube_shorts))
dispatcher.add_handler(CommandHandler("instareels", insta_reels))
dispatcher.add_handler(CommandHandler("spotify", spotify))
dispatcher.add_handler(CommandHandler("lyrics", lyrics))
dispatcher.add_handler(CommandHandler("ytmp3", youtube_mp
