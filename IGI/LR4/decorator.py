"""
Lab Work #1
Gordashuk Vladislav
This module implement decorator to repeat the task
Version: 1.0
Date: 30.03.2025
"""

def repeat_on_demand(prompt="Repeat? (1 - Yes, other - no): "):
    """
    Decorator to repeat task
    
    Args: prompt str
    """
    def decorator(func):
        def wrapper():
            while True:
                func()
                choice = input(prompt)
                if choice != '1':
                    print("Exit...")
                    break
                print("\n" + "="*40 + "\n") 
        return wrapper
    return decorator
