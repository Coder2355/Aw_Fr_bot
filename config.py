import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21740783")
    API_HASH  = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7766709030:AAEHnIF6EkNttAij4cOCZat74PMK5Ymm6is") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Speedwolf1")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/feb6dd0a1cb8576943c0f.jpg")
    ADMIN = [6299192020,6121610691,6693549185,5326198063, 7035627523] 
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'ATXBOTS').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002040299414"))
    PORT = int(os.environ.get("PORT", "8030"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced Video Uploader Bot.

➻ Using This Bot You Can Able to Upload Your Files.

➻ You Can Also Select the path where the file is need to upload.

➻ This Bot is only for dev👉 @Anime_warrior_Tamil[Awt_botz].

<b>Bot Is Made By :</b> @Anime_warrior_tamil"""

    ABOUT_TXT = f"""<b>😈 My Name :</b> <a href='https://t.me/Gjjbsrijjb_bot'>Video editor bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Anime_Warrior_Tamil'>AWT BOTS</a>
<b>🛡️ :</b> <a href='https://t.me/+NITVxLchQhYzNGZl'>AWT Developer</a>
    
<b>😈 Bot Made By :</b> @AWT_Bot_Developer"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `Now off❌`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @Anime_warrior_tamil</code>

💬 For Any Help Contact @Anime_warrior_tamil
"""
        
    
