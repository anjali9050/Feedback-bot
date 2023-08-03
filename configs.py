import os

class Config(object):

    API_ID = 23560088 #int(os.environ.get("API_ID", 12345))

    API_HASH = "999c01704d5c417749a98f4b8785fe88" #str(os.environ.get("API_HASH", ""))

    BOT_TOKEN = "6290477228:AAFyWeI_VU8Jx-oCqObhmUTs5en5dnGiawc" #str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = 5216454450 #int(os.environ.get("OWNER_ID", 1428968542))

    AUTH_USERS = set(int(x) for x in "1864861524".split())#set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    START = "Hey I'm a simple Telegram bot that can broadcast messages and media to the bot subscribers. Made by @BABA1920Prediction."#str(os.environ.get("START_TEXT", ""))

    HELP = "Help text" #str(os.environ.get("HELP_TEXT", ""))

    DONATE = "Donate text"#str(os.environ.get("DONATE_TEXT", ""))

    DONATE_LINK = "https://t.me/BABA1920Prediction"#str(os.environ.get("DONATE_LINK", ""))

    UPDATE_CHANNEL = "https://t.me/BABA1920Prediction" #str(os.environ.get("UPDATE_CHANNEL", ""))

    SUPPORT_GROUP = "https://t.me/BABA1920Prediction" #str(os.environ.get("SUPPORT_GROUP", ""))

    DB_URL = "mongodb+srv://baba:baba@cluster0.etssakc.mongodb.net/?retryWrites=true&w=majority" #str(os.environ.get("DB_URL", ""))
    
    DB_NAME = "BroadcastBot" #str(os.environ.get("DB_NAME", ""))
    
    LOG_CHANNEL = -1001958949068#int(os.environ.get("LOG_CHANNEL", ""))

    BROADCAST_AS_COPY = False #bool(os.environ.get("BROADCAST_AS_COPY", True))

