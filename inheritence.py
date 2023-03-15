class User:
     def login(self):
        print("login")

     def ragister(self):
        print("Ragister")

class Student(User):
    def enroll(self):
        print("Enroll")

    def review(self):
        print("review")

std1 = Student()

std1.review()
std1.enroll()
std1.ragister()