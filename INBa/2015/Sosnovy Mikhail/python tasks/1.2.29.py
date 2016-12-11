import math
a=float(input("1 сторона :"))
b=float(input("2 сторона :"))
c=float(input("3 сторона :"))
pp = (a+b+c)*0.5
print ('Площпдь равна', math.sqrt(pp*(pp-a)*(pp-b)*(pp-c)))