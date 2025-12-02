#print("Hello Everyone! We are learning python")
#name = input("Enter your name : ")
#age = int(input("Enter your age: "))
#print(name,age)

#print(max(1,2,3,5,9,10,20))
#print(min(1,2,3,4,3,212,122,))
#print(abs(-2020))
#print(pow(2,3))
"""
When all the length of sides of the triangle is know a,b,c
semipermeter (s) = (a+b+c) / 2
area = square root of (s *(s-a) * (s-b) * (s-c)
"""
a = float(input("Enter you First side: "))
b = float(input("Enter you Second side: "))
c = float(input("Enter you third side: "))
s = (a + b+ c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print(round(area,2))