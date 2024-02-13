# Class is a blueprint of an object
# Object is an instance of a class

class Person:
    #Properties/Attributes/Characteristics
    age = 23
    name = "Bill"
    # Method/Function/Behavior
    def talk(self):
        print("person is talking")


teacher = Person()
print(teacher.name)
print(teacher.age)

teacher.talk()