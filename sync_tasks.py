import threading
import time


def execute_sync_task(task_name : str,duration:int):
    print(f"Task is staring - {task_name}")
    time.sleep(duration)
    print(f"Task is ending - {task_name}")


def main():
    #Synchronous blocking code
    # execute_sync_task("Task 01",10)
    # execute_sync_task("Task 02",2)
    # execute_sync_task("Task 03",1)

    #Synchronous nonblocking code
    tread1= threading.Thread(target=execute_sync_task,args=("Task 01",5))
    tread2= threading.Thread(target=execute_sync_task,args=("Task 02",3))
    tread3= threading.Thread(target=execute_sync_task,args=("Task 03",1))

    tread1.start()
    tread2.start()
    tread3.start()


if __name__=="__main__":
    main()