class Person:
    def __init__(self, name , age ):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is" , self.age )

john = Person("John", 22)
lucy = Person ("lucy", 32)

john.print_info()
lucy.print_info()