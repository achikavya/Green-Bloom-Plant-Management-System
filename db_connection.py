import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "green_bloom_db")
        )

        if connection.is_connected():
            print("Connected to Green Bloom database successfully!")
            return connection

    except (Error, ValueError) as e:
        print("Database connection failed:", e)

    return None