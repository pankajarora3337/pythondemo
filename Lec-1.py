Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
True and True
True
False and False
False



True or False
True
False or True
True


False or False
False




not True
False
not False
True
name = "Pankaj"
age = 29
name == "Pankaj" and age >=25
True
name == "pankaj" or age >= 30
False
name == "Pankaj" or age >= 30
True



# Precedence in python
5 + 10 * 6
65
(5 +10) * 6
90




name = "Pankaj"
age = 29
name
'Pankaj'
age
29
name == "Pankaj" or name == "Mark" and age <=30
True
name == "Pankaj" or name == "Mark" and age >= 30
True


# And operator has higher precendence than OR
(name == "Pankaj" or name == "Neeraj" ) and age <=30
True
(name == "Pankaj" or name == "Neeraj" ) and age >= 30
False
100 / 10 * 20
200.0
# Associativity


2 ** 1 ** 3
2
#Classification of operators based on the number of operands
#Unary
-10
-10
not True
False
not False
True
>>> 
>>> #Binary Operator
>>> #Ternary
>>> #if-else
>>> print("pankaj"
...     )
pankaj
>>> num1 = 10
>>> print(num1)
10
>>> name = "John"
>>> age = 20
>>> print(age)
20
>>> print(name,age)
John 20
>>> print(10,20,30,40, sep="")
10203040
>>> print(10,20,30,40, sep=" $ "
...       )
10 $ 20 $ 30 $ 40
>>>  day = 10
...  
SyntaxError: unexpected indent
>>> day = 10
>>> month = 3
>>> year = 2025
>>> #10/3/2025
>>> print(day,month,year, sep"/")
SyntaxError: invalid syntax
>>> print(day,month,year, sep = "/")
10/3/2025
>>> #In input function as the name suggest is used to take an input from an user
>>> name = input(Name:)
SyntaxError: invalid syntax
>>> first_name = input()
Pankaj
>>> print(first_name)
Pankaj
