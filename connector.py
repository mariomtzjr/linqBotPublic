import psycopg2
import os

from dotenv import load_dotenv
from settings import path_dir_env


class Connect:
    load_dotenv(os.path.join(path_dir_env, '.env'))

    db = psycopg2.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
    )
