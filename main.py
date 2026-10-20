from connection import *
from service import *
import asyncio


async def main():
    await create_table()
    await registration()

    while True:
        n =int(input("1)Registration\n2)Create task\n3)Get task\n0)Exit\nChoose one: "))

        match n:
            case 1:
                name =input("Name: ")
                number =input("Number: ")
                password =input("Password: ")

                await registratio(name, number,password)


            case 2:
                title =input("Title: ")
                descp =input("Description: ")
                due_date =input("Due date: ")

                await create_task(title, descp,due_date)

            case 3:
                await get_task()

            case 0:
                break

            case _:
                print("Invalid input")


if __name__ == "__main__":
    asyncio.run(main())
