import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "20980764").strip()
API_HASH = os.getenv("API_HASH", "e7ee72bff6d00b1e00987f968136b7e8").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6670342404:AAHwMhGtlwGdl7ys4vcF_w03jviSgO7EYxM").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kaushalxraja:JSck0@cluster0.dfvemtb.mongodb.net/?retryWrites=true&w=majority").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "Amit_xcb")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
