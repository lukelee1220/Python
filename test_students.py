class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("I am", self.name, " And"," I am", self.age )


class Student_Sport(Student):

    def sport(self):
        print(self.name," likes Swimming !!!")

maidou = Student("Maidou", 11)
Luke = Student("Luke", 9)

maidou.introduce()
Luke.introduce()

Luke1 = Student_Sport("Luke", 9)
Luke1.introduce()
Luke1.sport()
maidou.sport()