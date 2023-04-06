from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a bot.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    updater = Updater(token='YOUR_TOKEN', use_context=True)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()

    
import youtube_dl

def download_youtube_shorts(update, context):
    url = context.args[0]

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'short.mp4',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    context.bot.send_video(chat_id=update.effective_chat.id, video=open('short.mp4', 'rb'))

    
import instaloader

def download_instagram_reel(update, context):
    url = context.args[0]

    L = instaloader.Instaloader()

    L.download_video(url, filename='reel.mp4')

    context.bot.send_video(chat_id=update.effective_chat.id, video=open('reel.mp4', 'rb'))
