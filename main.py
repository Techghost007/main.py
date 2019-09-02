# print("Hi Shubham!")
# print("5+8")
# #Comment
# a=12
# if a<18:
#     print("You are young :D")
# else:
#     print("You are old ")

# import math
# print(math.gcd(3,6))

# a = 34
# b = "Shubham"
# c = 45.578
# print(a+c)
# print(a**c)

# z = "12"
# z = float(z)
# z = str(erer)
# print(z+2)

# s = 33
# s = str(s)
# print(s+" gf")
# import math
# a = math.log2(3)
# print(a)
#  b = math.log(3,2)
#  print(b)


# a = 2
# b = 3
# a,b = b,a
# print(a)
# print(b)

# a = [2,33,5,67,54]
# a = type(a)
# print(a)
# import math
# z = 49
# print(math.sqrt(z))

# import time 
# from datetime import date
# x = date.today()
# print(x)

# my_birthday = date(1995, 2, 19)
# print(my_birthday)



# x = 100
# if x/2 == 50:
#     print( "even number")
# else:
#     print("odd number")

# list = [1,2,3,4,5]
# it = iter(list)
# print(next(it))

# name = "Harry Boy!"
# print(name[2::])
# print(name.strip())
# print(len(name))

# var = name.lower()
# uvar = name.upper()
# print(var)
# print(uvar)
# ab = name.replace(" ", '\n')

# stra = "This "
# strb = "That "
# print(stra + strb)
# temp = "Who's {}& What's {}".format(stra, strb)
# temp = f"Who's {stra}& What's {strb}"
# print(temp)

# q = 10
# w = 20 
# r = 30 
# print(q**w)
# print(r//q)
# print(r%w)

# xyz = 5%2
# print(xyz)

# t = int(input("Enter the No.:" ))
# if t%2 == 0:
#     print("Even number.")
# else:
#     print("Odd number.")
'''
Python Collection
1. List
2. Tuple
3. Set
4. Dictionary

'''
# lst = [1,2,3,56,4,44,66]
# var = type(lst)
# print(var)
# print(lst[2::])
# lst.sort()
# print(lst)
# lst[3] = 55.5
# lst[5] = "23"
# lst.append(99)
# lst.insert(4, 58)
# lst.pop(5)
# print(lst)
# print(len(lst))

# tpl = ("asd", "qwe", "zxc")
# print(type(tpl))
# print(tpl)
# tuple.count(tpl)

# Result = {
#     "Name" : "Shubham",
#     "Degree" : "B.Tech",
#     "Division" : "1st Class",
#     "Percentage" : 85
# }
# Result.update({"Remarks" : "Pass"})
# print(Result["Remarks"])

# age = int(input("Abe Apni Age bata:\n"))
# print(age)

# for i in range(0,1000):
#     print(i)

# for item in lst:
#     print(item)
#     # lst.sort()
#     # lst.reverse()

# y = 1
# while(y<20):
#     print(y)
#     y = y+1

# def greet():
#     print("Good Morning!")

# greet()

# def sum(a,b):
#     c = a + b
#     print(c)

# sum(23.43, 45)
"""
1. Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""
# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())
# if n%2 != 0:
#     print("Weird") 
# else:
#     if 2<=n<=5:
#         print("Not Weird")
#     if 6<=n<=20:
#         print("Weird")
#     if n>20:
#         print("Not Weird")   

"""
2. Task 
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
# print(a+b)
# print(a-b)
# print(a*b)

"""
3. Task 
Read two integers and print two lines. The first line should contain integer division, a // b. 
The second line should contain float division, a / b.

You don't need to perform any rounding or formatting operations.

"""
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
# print(a//b)
# print(a/b)

"""
4. Task 
Read an integer N. For all non-negative integers i<N, print (square of i). 
"""
# if __name__ == '__main__':
#     n = int(input())
# for i in range(0,n):
#     print(i**2)
#     i = i+1

"""
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

5. Task 
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.


"""

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if (year%4) == 0:
#         if (year%100) == 0:
#             if (year%400) == 0:
#                return True
#             else:
#                 return leap
#         else:
#             return True        
#     else:
#         return leap

# year = int(input())
# print(is_leap(year))

"""
Read an integer N.

Without using any string methods, try to print the following:

123...N
Note that "..." represents the values in between.

"""

# if __name__ == '__main__':
#     n = int(input())
# for i in range (0,n):
#     i = i+1
#     print(i, end = "")

"""
A valid postal code P have to fullfil both below requirements:

P must be a number in the range from 100000 to 999999 inclusive.
P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:

regex_integer_in_range should match only integers range from 100000 to 999999 inclusive

regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.

Both these regular expressions will be used by the provided code template to check if the input string  is a valid postal code using the following expression:

(bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
"""

# regex_integer_in_range = r"_________"	# Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.


# import re
# P = input()

# print (bool(re.match(regex_integer_in_range, P)) 
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

P = int(input())
for P in range (100000, 999999):
    if P[0] == P[2]:
        return False
