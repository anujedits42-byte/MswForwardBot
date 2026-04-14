from os import environ 

class Config:
    API_ID = environ.get("API_ID", "34446649")
    API_HASH = environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6558508467Fy7bWSpD-2qd-LPH9tAnL2GW8T1Qe4") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0"
    DATABASE_NAME = environ.get("DATABASE_NAME", "Anujedit")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7892805795').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
