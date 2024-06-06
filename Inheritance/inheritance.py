class Student:
    age=16
    
std=Student()
print(std.age)

# classes and objects in python
class Student:
    def __init__(person,name,age):
        person.name=name
        person.age=age
        
std=Student("Alison",20)
print(std.name)
print(std.age)

#__str__() function controls what should be returned when the class object is represented as a string
class Student:
    def __init__(person,name,age):
        person.name=name
        person.age=age
        
std=Student("Alison",20)
print(std)   #CHECK THIS OUT, it will return  <__main__.Student object at 0x000001A31F9C6030>

#Using __str__() function 

class Animal:
    def __init__(breed,state,status):
        breed.state=state
        breed.status=status
    def __str__(breed): 
        return f"{breed.state}({breed.status})"  
    def printDetails(breed):
        print(breed.status + " and its from " + breed.state)
    
mammal=Animal("Texas", "healthy")
mammal.state="Calabasas"

print(mammal)
mammal.printDetails()




        

        
         