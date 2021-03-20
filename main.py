#!/usr/bin/env python3


def add(x,y):
	return x+y

try:

   num1,num2=(input("enter 2 number : ")).split( )
   w=int(num1)
   n=int(num2)
   choice = input("Do you want to add the two integers - Type yes / no :  ")
   z=add(w,n)

except (ValueError):

   print("Please input  2 numbers !")
   num1,num2=(input("enter 2 number")).split( )
   w=int(num1)
   n=int(num2)
   z = add(w,n)
   choice = input("Do you want to add the two integers - Type yes / no  :  ")


if (choice=="yes"):

  print("The sum : ",z)

else:
    print("Your num1 is : ", w)
    print("Your num2 is : ", n)
