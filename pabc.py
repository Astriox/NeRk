import telegram
import logging
import youtube_dl
import spotipy
import requests
import os
import re
import json
import urllib.parse
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Create the bot and set up logging
bot = telegram.Bot(token='YOUR_TOKEN_HERE')
updater = Updater(token='YOUR_TOKEN_HERE', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the handlers for each feature
def youtube_shorts_downloader(update, context):
    chat_id = update.effective_chat.id
    url = context.args[0]
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.filter(file_extension='mp4', res='360p').first()
        video.download()
        bot.send_message(chat_id=chat_id, text='Downloaded!')
    except Exception as e:
        bot.send_message(chat_id=chat_id, text='Error: {}'.format(str(e)))

def instagram_reels_downloader(update, context):
    chat_id = update.effective_chat.id
    url = context.args[0]
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.filter(file_extension='mp4', res='360p').first()
        video.download()
        bot.send_message(chat_id=chat_id, text='Downloaded!')
    except Exception as e:
        bot.send_message(chat_id=chat_id, text='Error: {}'.format(str(e)))

def spotify_downloader(update, context):
    chat_id = update.effective_chat.id
    spotify = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', redirect_uri='YOUR_REDIRECT_URI', scope='user-library-read'))
    query = context.args[0]
    result = spotify.search(query, type='track')
    try:
        track_id = result['tracks']['items'][0]['id']
        track_name = result['tracks']['items'][0]['name']
        track_artist = result['tracks']['items'][0]['artists'][0]['name']
        track_album = result['tracks']['items'][0]['album']['name']
        track_url = result['tracks']['items'][0]['external_urls']['spotify']
        audio = spotify.audio_features(track_id)
        audio
