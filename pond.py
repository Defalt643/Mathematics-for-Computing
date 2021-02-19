h=int(input("Enter hour(s) :"))
m=int(input("Enter minute(s) :"))
s=int(input("Enter second(s) :"))
print((h*60*60)+(m*60)+s,"seconds")
import math
x=int(input("Enter value of x : "))
print("y = ",(2-x+((3/7)*x**2)-((5/11)*x**3)+math.log(x,10)))

a=int(input("Enter value of x : "))
x=1;
for i in range (4):
    x=(x+a/x)/2
print("x = ",x)


def f1(a,b):
    for i in range(b):
        print(a)
f1(input(),int(input()))




