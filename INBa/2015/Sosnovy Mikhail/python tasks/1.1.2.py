import math
p=int(input("Число p:"))
y=int(input("Число y:"))
e=int(input("Число e:"))
k = math.log2(p**2+y**3) + e**p
print (k)