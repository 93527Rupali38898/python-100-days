# hybrid inheritance
class User:
    def login(self):
        print("User login")
    def logout(self):
        print("User logout")
class Student(User):
    def enroll(self):
        print("Student enrolled")
    def drop(self):
        print("Student dropped")
class Instructor(User):
    def assign(self):
        print("Instructor assigned")
    def grade(self):
        print("Instructor graded")
class TA(Student,Instructor):
    def answer(self):
        print("TA answered")
    def review(self):
        print("TA reviewed")
ta=TA()
ta.login()
ta.logout()
ta.enroll()
ta.drop()
ta.assign()
ta.grade()
ta.answer()
ta.review()


# heirarchical inheritance
class User:
    def login(self):
        print("User login")
    def logout(self):
        print("User logout")
class Student(User):
    def enroll(self):
        print("Student enrolled")
    def drop(self):
        print("Student dropped")
class Instructor(User):
    def assign(self):
        print("Instructor assigned")
    def grade(self):
        print("Instructor graded")
class TA(User):
    def answer(self):
        print("TA answered")
    def review(self):
        print("TA reviewed")
student=Student()
student.login()
student.logout()
student.enroll()
student.drop()
instructor=Instructor()
instructor.login()
instructor.logout()
instructor.assign()
instructor.grade()
ta=TA()
ta.login()
ta.logout()
ta.answer()
ta.review()