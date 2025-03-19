import pygame
pygame.init()

namee=input("Enter student's name:")
ages=input("Enter student's age")


class Student():
    def __init__(self, name, age):
        self.name=namee
        self.age=ages

string_value = ages
integer_value = int(string_value)

if integer_value > 12:
    print("{} is in secondary school.".format(namee))
else:
    print("{} is in primary school.".format(namee))