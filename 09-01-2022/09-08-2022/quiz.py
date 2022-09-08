import math
import numpy as np
import matplotlib.pyplot as plt

class Triangle:
    def __init__(self, a, b, c):
        self.a = a #where a is the length of a side
        self.b = b #where b is the length of a side
        self.c = c #where c is the length of a side
    def Areac(self):
        s = (self.a + self.b + self.c)/2
        inte = s*(s - self.a)*(s - self.b)*(s - self.c)
        Area_calc = math.sqrt(inte)
        return Area_calc
    def Perimeterc(self):
        peri = self.a +self.b+self.c
        return peri
    def Angle(self):
        determinantc = 2 * self.a * self.b
        C_num = math.pow(self.a, 2) + math.pow(self.b, 2) - math.pow(self.c, 2)
        C_angle_n = C_num/determinantc
        anglec = math.acos(C_angle_n)
        determinantb = 2 * self.c * self.a
        B_num = math.pow(self.c, 2) + math.pow(self.a, 2) - math.pow(self.b, 2)
        B_angle = B_num/determinantb
        angleb = math.acos(B_angle)
        determinanta = 2 * self.c * self.b
        A_num = math.pow(self.c, 2) + math.pow(self.b, 2) - math.pow(self.a, 2)
        A_angle = A_num/determinanta
        angleA = math.acos(A_angle)
        return angleA, angleb, anglec

#The main program
answer_quest = "yes"
while(answer_quest == "yes"):
    a, b, c = input("Please type the side of your angle: ").split()
    a = float(a)
    b = float(b)
    c = float(c)
    trian = Triangle(a,b,c)
    peri_ta = trian.Perimeterc()
    A,B,C = trian.Angle()
    Area_cal = trian.Areac()
    print("The area of the triangle is {}".format(Area_cal))
    print("The Perimeter of the triangle is {}".format(peri_ta))
    print("The angles of the triangle are A = {}, B = {}, C = {}".format(A,B,C))


    answer_quest = input("\nDo you want to keep using the application? ")