class Student():
    def __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname

    def name(self):
        return self.fname + ", " + self.lname

class Werkstudent(Student):
    def __init__(self, fname, lname, job):
        super().__init__(fname, lname)
        self.job=job

    def name(self):
        return self.fname + " " + self.lname + " ist ein Werkstudent"

student1=Student("max", "mustermann")
print(student1.name())
werkstudent1=Werkstudent("Erik", "Müller","Kellner")
print(werkstudent1.job)
print(werkstudent1.name())
# die Methode aus der Elternklasse wurde ersetzt durch die Methode aus der
# Subclass - beide Methoden haben denselben namen "name"
# um die Methode aus Elternklasse aufzurufen:
# return super().name() + "("self.job")" -> in Subclass
# students = [werkstudent("max", "müller", "kellner"), student("anna", "mustermann"),
# werkstudent("tom","schmidt","helfer"), student("melani", "mustermann")]
# for student in students:
#   print(student.name())
