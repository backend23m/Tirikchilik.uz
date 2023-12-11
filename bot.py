from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
API   = os.getenv('API')

print(TOKEN)
print(API)
print(os.getenv('USER'))

print(os.getcwd())
