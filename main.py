#18-m
class Universty:
        def __init__(self, name, students):
            self.name = name
            self.__students = students

        def get_students(self):
            return self.__students

        def set_students(self, new_students):
            if new_students > self.__students:
                self.__students = new_students
            else:
                print("Talabalar soni oshishi kerak")
                
u1 = Universty("TATU", 15000)

print(u1.name)
print(u1.get_students())

u1.set_students(15008)
print(u1.get_students())

u1.set_students(15007)
print(u1.get_students())
