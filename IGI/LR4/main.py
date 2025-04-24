from task1 import Task1
from task2 import Task2
from task3 import Task3
from task4 import Task4
from task5 import Task5
from decorator import repeat_on_demand


"""
Lab Work #2
Gordashuk Vladislav
This module processes task selection
Version: 1.0
Date: 23.04S.2025
"""

def PrintMenu():
    """Display menu"""
    print("\n" + "="*40)
    print("Choose task")
    print("1 - Task 1")
    print("2 - Task 2")
    print("3 - Task 3")
    print("4 - Task 4")
    print("5 - Task 5")
    print("6 - End")

PrintMenu()
while True:
    flag = input()
    if flag == '1':
        Task1()
        PrintMenu()
    elif flag == '2':
        Task2()
        PrintMenu()
    elif flag == '3':
        Task3()
        PrintMenu()
    elif flag == '4':
        Task4()
        PrintMenu()
    elif flag == '5':
        Task5()
        PrintMenu()
    elif flag == '6':
        exit()
    else:
        print("Wrong num")    
