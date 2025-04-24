class Student:
    def __init__(self, name: str, run: float, jump: float):
        self.name = name
        self.run = run
        self.jump = jump
    def __repr__(self):
        return f"Name - '{self.name}', 100m - {self.run}, jump - {self.jump})"