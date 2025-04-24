from Student import Student 

class TRPNormAnalyz:
    def __init__(self, students: list[Student], run_standard: float, jump_standard: float):
        self.students = students
        self.run_standard = run_standard
        self.jump_standard = jump_standard

    def not_pass(self) -> list[Student]:
        """
        Checks who hasn't passed the norm
        Returns:
            list[Student]: not passed
        """
        return [student for student in self.students if student.run > self.run_standard or student.jump < self.jump_standard]
    
    def passed(self) -> int:
        """
        Count how many passed the norm
        Returns:
            int
        """
        return len([student for student in self.students if student.run <= self.run_standard or student.jump >= self.jump_standard])
    
    def top3_jump(self) -> list[Student]:
        """
        Find best students in jump
        Returns:
            list[Student]: top 3
        """
        return sorted(self.students, key=lambda x: x.jump)[:3]
    
    def top3_run(self) -> list[Student]:
        """
        Find best students in run
        Returns:
            list[Student]: top 3
        """
        return sorted(self.students, key=lambda x: x.run)[:3]
        
    def get_student(self, name: str):
        """
        Find student for name
        Args:
            name (str): student name

        Returns:
            Student
        """
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None