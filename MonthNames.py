# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year. An example run of the program (numbers in bold are typed in by the user) Enter the month: 3 Month 3 is March

'''

number=int(input('Enter the number'))


if number in range(1,13):

        if number == 1:
            print(f"month {number} is {'january'}.")
        elif number==2:
            print(f"month {number} is {'february'}.")
        elif number==3:
            print(f"month {number} is {'March'}.")
        elif number==4:
            print(f"month {number} is {'April'}.")
        elif number==5:
            print(f"month {number} is {'May'}.")
        elif number==6:
            print(f"month {number} is {'june'}.")
        elif number==7:
            print(f"month {number} is {'July'}.")
        elif number==8:
            print(f"month {number} is {'August'}.")
        elif number==9:
            print(f"month {number} is {'September'}.")
        elif number==10:
            print(f"month {number} is {'October'}.")
        elif number==11:
            print(f"month {number} is {'November'}.")
        elif number==12:
            print(f"month {number} is {'December'}.")

else :
    print('Invalid number')

'''
from itertools import count

# Exercise 2
# A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old,
# and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user)
# Enter your age: 63 Your ticket costs £2.00
'''Price=6
age=int(input('Enter The Age:'))
if age<16:
    Ticketprice=.5*Price
elif age>60:
    Ticketprice=1/3* Price
else:
    Ticketprice=Price
print(f'your ticket Costs { Ticketprice} Pounds')


'''
# Exercise 4
# Write a Python program to receive 3 numbers from the user and print the greatest among them.
'''
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if x>=y and x>=z:
    greatest_number=x
elif y>=x and y>=z:
    greatest_number=y
else:
    greatest_number=z
print(f"biggest number is {greatest_number}")

'''

# Exercise 5
# Find the factorial of a given number using loops(note the number is received from the user)
'''
x=int(input('Enter the number' ))
fact=1
if x==0 and x==1:
    print(f"factorial is 1")
else:
    for i in range(1,x+1):
        fact*=i
    print(f"the factorial of {x} is {fact}")
'''
# Exercise 6
# Reverse a number using while loop
'''
while True:
    num=int(input("Enter the number:"))
    rev_num=0
    while num > 0:
        reminder = num % 10
        rev_num = (rev_num*10)+reminder
        num=num//10
    print(f"The reversed Number is {rev_num} ")

#The below one  will finish after one execution
num=int(input("Enter the number:"))
rev_num=0
while num > 0:
        reminder = num % 10
        rev_num = (rev_num*10)+reminder
        num=num//10
print(f"The reversed Number is {rev_num} ")
'''

# Exercise 7
# Finding the multiples of a number using loop
'''
num=int(input('Enter the Number'))
count=int(input('number of count'))
for i in range (1,count+1):

        print(i*num)
'''

# Exercise 8
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
'''
while True:
    x=input('Enter something:')
    if x.lower()== 'done':
        print('Done')
        break
    print(x)
'''

# Exercise 9
# Write a program that prints the numbers from 1 to 10.
# But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
'''
for i in range(1,20):
    if i%3==0 and i%5==0:
        print('Fizz buzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0 :
        print('Fizz')
    else:
        print(i)
'''
# Exercise 10
# Write a program to print the following pattern: 5 4 3 2 1 4 3 2 1 3 2 1 2 1 1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
