#!/usr/bin/env python3

def mul(x,y):
    return x*y



try:

    num1,num2=(input("Entrez 2 nombres :")).split( )
    w=int(num1)
    n=int(num2)
    z=mul(w,n)
    print("The mul : ", z)

except (ValueError):
    print("please entrez 2 nombres svp :")
    num1,num2=(input("Entrez 2 nombres :")).split( )
    w=int(num1)
    n=int(num2)
    z=mul(w,n)
    print("The mul : ", z)
except (ValueError):
    print("please entrez 2 nombres svp :")
    num1,num2=(input("Entrez 2 nombres :")).split( )
    w=int(num1)
    n=int(num2)
    z=mul(w,n)
    print("The mul : ", z)

