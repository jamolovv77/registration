
from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

pasw =os.getenv("PASSWORD_DB")


async def connection_db():
    conn =await asyncpg.connect(
        port=5432,
        host="localhost",
        user="postgres",
        database="task_db",
        password=pasw
    )

    print("Connection successful")
    return conn


async def create_table():
    conn =await connection_db()

    try:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS task (
                task_id SERIAL PRIMARY KEY,
                title VARCHAR(200),
                description TEXT,
                due_date VARCHAR(50),
                status BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT NOW(),
                is_active BOOLEAN DEFAULT TRUE
            )
        """)

        print("Created task table successful")

    finally:
        await conn.close()


async def registration():
    conn =await connection_db()

    try:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS reg (
                registration_id SERIAL PRIMARY KEY,
                name VARCHAR(144),
                number_fhone VARCHAR(144),
                password VARCHAR(144)
            )
        """)

        print("Created registration table successful")

    finally:
        await conn.close()