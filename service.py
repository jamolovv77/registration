from connection import *


async def create_task(title, descp, due_date):
    conn = await connection_db()

    try:
        await conn.execute("""
            INSERT INTO task (title, description, due_date)
            VALUES ($1, $2, $3)
        """, title, descp,due_date)

        print("Created task successful")

    except Exception as Error:
        print(f"Create task Error: {Error}")

    finally:
        await conn.close()


async def get_task():
    conn =await connection_db()

    try:
        tasks =await conn.fetch("""
            SELECT * FROM task
        """)

        for task in tasks:
            print(f"""
Task id: {task["task_id"]}
Title: {task["title"]}
Description: {task["description"]}
Duration date: {task["due_date"]}
""")

        return tasks

    except Exception as Error:
        print(f"Get task Error: {Error}")

    finally:
        await conn.close()


async def registratio(name,number_fhone,password):
    conn =await connection_db()

    try:
        await conn.execute("""
            insert into reg (name, number_fhone, password)
            VALUES ($1, $2, $3)
        """, name,number_fhone,password)

        print("Registration successful")

    except Exception as Error:
        print(f"Registration Error: {Error}")

    finally:
        await conn.close()
