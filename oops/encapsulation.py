# example using encapsulation (student login details)

class Student:
    def __init__(self,stu_name,stu_pass):
        self.__name=stu_name
        self.__pass=stu_pass
    def login(self,c_pin):
        if c_pin == c_pin:
            print(f"Student {self.__name} login successfully")
        else:
            print(f"Student {self.__name} login failed")
a3=Student("vamsi",8897)
current_pin=input("enter your pin")
a3.login(current_pin)