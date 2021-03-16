#!/usr/bin/env python3
def add(x,y):
	return x+y

try:
	num1,num2= (input("enter 2 number")).split( )
	w=int(num1)
	n=int(num2)
	z = add(w,n)
	print("The SUM : ",z)

except (ValueError):
	print("Please input only 2 numbers only !")


