from Analyz import TRPNormAnalyz
from Student import Student
from decorator import repeat_on_demand
from serializer import Serializer
import os

def generate_sample_data():
    """Generate data"""
    return [
        {"name": "Иванов Иван", "run": 12.5, "jump": 4.2},
        {"name": "Петров Петр", "run": 13.8, "jump": 3.9},
        {"name": "Сидорова Анна", "run": 11.9, "jump": 4.5},
        {"name": "Кузнецов Алексей", "run": 14.1, "jump": 3.7},
        {"name": "Смирнова Мария", "run": 12.8, "jump": 4.1},
        {"name": "Васильев Дмитрий", "run": 13.5, "jump": 3.8},
        {"name": "Николаева Елена", "run": 12.2, "jump": 4.3},
        {"name": "Федоров Сергей", "run": 14.3, "jump": 3.5},
        {"name": "Павлова Ольга", "run": 11.7, "jump": 4.6},
        {"name": "Александров Андрей", "run": 13.2, "jump": 3.9}
    ]

def prepare_files():
    """Create files"""
    filename = "students"
    sample_data = generate_sample_data()
    Serializer.write_pickle(sample_data, filename + ".txt")
    Serializer.write_csv(sample_data, filename + ".csv")

@repeat_on_demand()
def Task1():
    """Load data from file and analizy it"""
    if not os.path.isfile("students.txt") or not os.path.isfile("students.csv"):
        prepare_files()
    
    filename = "students"
    while True:
        print("1 - Load from pickle")
        print("2 - Load from csv")
        flag = input()
        if flag == '1':
            students_from = Serializer.read_pickle(filename + ".txt")
            students = [Student(s['name'], s['run'], s['jump']) for s in students_from]
            break
        elif flag == '2': 
            students_from = Serializer.read_csv(filename + ".csv")
            
            students = [Student(item['name'], float(item['run']), float(item['jump'])) 
                for item in students_from]
            break
    
    trpAnalyz = TRPNormAnalyz(students, 13, 4)
    print("\n" + "="*40)
    print("Passed -", trpAnalyz.passed(), "students")
    print("\n" + "="*40)
    print("Didn't pass -", trpAnalyz.not_pass(), "students")
    print("\n" + "="*40)
    print("Top 3 students -", trpAnalyz.not_pass())
    print("\n" + "="*40)
    
    while True:
        print("Input student name or '1' to escape")
        inp = input()
        if inp == '1':
            print("Ending...")
            print("\n" + "="*40)
            return
        else:
            st = trpAnalyz.get_student(inp)
            if st is None:
                print("There is no student with that name")
                print("\n" + "="*40)
            else:
                print(st)
                print("\n" + "="*40)