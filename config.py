from dotenv import load_dotenv
from os import path, environ, getenv


load_dotenv("dev.env")

BOT_TOKEN = getenv('BOT_TOKEN')

OPENAI_API = environ.get('OpenAI_API')

SCRIPT_PATH = path.dirname(path.realpath(__file__)).split(sep='\\')

PROMPT_DATA_PATH = '\\'.join(SCRIPT_PATH + ['prompt\\data'])

PROMPT_INDEX_PATH = '\\'.join(SCRIPT_PATH + ['prompt\\index.json'])
