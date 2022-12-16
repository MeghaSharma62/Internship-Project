# import turtle
# # pen = turtle.Turtle()

# turtle.speed(10)
# turtle.bgcolor('black')
# turtle.pensize(3)
# def func():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)

# turtle.color("red","red")
# turtle.begin_fill()
# turtle.left(140)
# turtle.forward(111.65)
# func()
# turtle.left(120)
# func()
# def txt():
#     turtle.up()
#     turtle.setpos(-65, 100)
#     turtle.down()
#     turtle.color('lightgreen')
#     turtle.write("Swati", font=("Verdana", 12, "bold"))
#     # turtle.up()
#     turtle.down()
#     turtle.setpos(95,-68)
#     turtle.up()
#     turtle.color('aqua')
#     turtle.write("Love",font=("Verdana",12,'bold'))

# turtle.forward(111.65)
# turtle.end_fill()
# turtle.hideturtle()
# txt()
# # turtle.write("megha",font=("Verdana", 12, "bold"))
# turtle.done()

# i=10
# while i>=1:
#     print(i)
#     if i==6:
#         break
#     i-=1


# S1 = {10,20,30,40,50}
# S2 = {30,40,50,60,70}
# # Solution: -
# S3=S1.symmetric_difference(S2)
# print(S3)
# n=str(input("Enter the name:"))
# c=int(len(n)/2)
# d=n[0]+n[c-1]+n[-1]
# print(d)

# str1=input("enter the name")

# str2=""

# x=int(len(str1))

# for i in range(len(str1)):

#     if i==0 or i==x//2 or i==x-1:

#         str2+=str1[i]

# print(str2)


# Str1 = "WElcome"
# o/p: lcomeWE
# Solution: -
# b=[]
# c=[]
# for i in Str1:
#     if i.islower():
#         b.append(i)
#     else:
#         c.append(i)
#     d=b+c
# e="".join(d)
# e="".join(d)
# print(e)

# class Vehicle:
#     def __init__(self,Type,milege,model):
#         self.Type=Type
#         self.milege=milege
#         self.model=model

# class Bus(Vehicle):
#     def __init__(self,Type,milage,model,pas_capacity,buildyear):
#         Vehicle.__init__(self,Type,milage,model)
#         self.pas_capacity=pas_capacity
#         self.buildyear=buildyear
# vehicle=Bus("bus",25,"old",50,2002)
# print(vehicle.milege,vehicle.buildyear)
# print(vehicle.model)
# def outer_fun(a, b):
    
#     def addition(a, b):
#         return a + b

#     add = addition(a, b)
#     return add + 5

# print(outer_fun(20,15))


# 2. Write a program to define a student class that has the following attributes:
# - Name
# - Student ID
# - Marks
# The class must have a method to display the details.
# Also create an object that calls the method to display the details

# class Student:
#     def __init__(self,name,studentID,marks):
#         self.__name=name
#         self.studentID=studentID
#         self.marks=marks
#     def student_details(self):
#         return (self.name,self.studentID,self.marks)
# stu=Student("Megha",123,90)
# print(stu.marks)
# print(stu.name)


# a="Hii"
# def num():
#     global b
#     b="Hello"
# num()
# print(a)

# # Local Variable
# def sum():
#     d="local"
#     print(d)
# sum()

# class Mobile:
#     def __init__(self,brand,model,price):
#         self.__brand=brand
#         self.__model=model
#         self.__price=price
#     def get_brand(self):
#         return self.__brand
#     def get_model(self):
#         return self.__model
#     def get_price(self):
#         return self.__price
#     def set_price(self,new_price):
#         self.__price=new_price
#     def call (self,mobile_number):
#         print("calling to",mobile_number)
#     def discount(self,discount_amt):
#         self.price-=discount_amt
# info=Mobile("vivo","v25",25000)
# print(info.get_brand())
# info.set_price(30000)
# print(info.get_price())
# a=int(input("Enter the variable:-"))
# v=a
# print(type(v))

# n=input("Enter any string:")
# c=n.split('#')
# for i in c:
#     print(i)
# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(tuple1)


# def Sort_Tuple(tup):
#     # getting length of list of tuples
#     lst = len(tup)
#     for i in range(0, lst):
#         for j in range(0, lst-i-1):
#             if (tup[j][1] > tup[j + 1][1]):
#                 temp = tup[j]
#                 tup[j]= tup[j + 1]
#                 tup[j + 1]= temp
#     return tup
# import matplotlib as plt
# x = [2,3,4,5,6]
# y = [44,55,66,22,11]
# plt.figure(figsize = (10,10))
# plt.title("A simple graph")
# plt.plot(x,y,color = "brown",linewidth = 7,marker = 'o',ms = 20,mfc = "blue")
# plt.xlabel('Temp')
# plt.ylabel('sensor')
# plt.grid(color = "yellow",linewidth = 2)
# plt.show()
# a=[100,200]
# a.sort(reverse=True)
# print(a)


