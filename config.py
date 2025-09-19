from dotenv import load_dotenv
import os

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
NINJA_HOST = os.getenv("NINJA_HOST")
TWINWORD_HOST = os.getenv("TWINWORD_HOST")

NINJA_URL = f"https://{NINJA_HOST}/v1/sentiment"
TWINWORD_URL = f"https://{TWINWORD_HOST}/analyze/"