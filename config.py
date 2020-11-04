import os

class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("API_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      OWNER = [os.environ.get("OWNER_ID",  "")]
      PASS = os.environ.get("PASSWORD", "")
      RULES = os.environ.get("RULES", "")
      START = os.environ.get("START", "")
      SEND = []
      LOGIN = []
      feedback = []
