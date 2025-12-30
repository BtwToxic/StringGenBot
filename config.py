from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = 21705136
API_HASH = "78730e89d196e160b0f1992018c6cb19"

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"

OWNER_ID = 6944519938
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/techbotss")
