
import asyncio


async def execute_sync_task(task_name : str,duration:int):
    print(f"Task is staring - {task_name}")
    await asyncio.sleep(duration)
    print(f"Task is ending - {task_name}")


async def main():
    await asyncio.gather(
        execute_sync_task("Task 01",5),
        execute_sync_task("Task 02",3),
        execute_sync_task("Task 03",1),
    )

if __name__ == "__main__":
    asyncio.run(main()) # Initiating our event loop to execute the program