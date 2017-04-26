
#https://www.youtube.com/watch?v=irf2ekfkK0Q&list=PLvItDmb0sZw_MVK2txwtBSHAzaYRrOdiJ#t=1630.426449
class Person:
    def __init__(self, name , age):
        self.name  = name 
        self.age = age 


    def print_info(self):
        print(self.name, "is", self.age)

john = Person("john", 22)
lucy = Person("Lucy", 21)



john.print_info()
lucy.print_info()

class MyObject: 
    class_attribute = 9 

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print (self.data_attribute)

    @staticmethod
    def static_method():
        print(MyObject.class_attribute)
if __name__ == "__main__": 
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()