from dotenv import load_dotenv
import os

# Find .env file with os variables
load_dotenv("dev.env")

# retrieve config variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
