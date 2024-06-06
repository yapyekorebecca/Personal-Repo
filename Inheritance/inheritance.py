# class Student:
#     age=16
    
#     std=Student()
#     print(std.age)
class Student:
    def __init__(person,name,age):
        person.name=name
        person.age=age
        
        std=Student("Alison","20")
        print(std.name)
        print(std.age)
         