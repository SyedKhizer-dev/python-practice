class Student:
    subject = ("cs",)
    college = ("Reva",)
    add_year = 2023

    def __init__(self, name):
        self.name = name


stud1 = Student("SYED")
stud2 = Student("KHIZER")
print(stud1.subject, stud1.college, stud1.add_year)
print(stud2.subject, stud2.college, stud2.add_year)
