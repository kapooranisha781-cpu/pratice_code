# 1.Write a program to check whether a number is even or odd.
# num = 9
# if num % 2 == 0:
#     print("Even number")
# else: 
#     print("Odd number")


#  2.Write a program to check whether a person is eligible to vote (age ≥ 18).
# age = 17
# if age>18:
#     print("eligible for vote")
# else:
#     print("not eligible for vote")


#   3.Write a program to check if a number is divisible by 5.

# num = 45
# if num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("not divisible by 5")











# text = "madam"  
# is_palindrome = True
# i = 0
# j = len(text) - 1
# while i < j:
#     if text[i] != text[j]:
#         is_palindrome = False
#         break
#     i += 1
#     j -= 1
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")














# 00PS

# class
# class Animal:
#     def sound(self):
#         print("Animal makes sound")


# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")


# d1 = Dog()

# d1.sound()
# d1.bark()










# arr = [10,20,30,40,50]
# print(arr[2])




# arr = []

# arr.append(10)
# arr.append(20)
# arr.append(30)
# arr.append(40)
# arr.append(50)
# arr.remove(arr[2])
# print(arr)





# PRINT NUMBER 1 TO 5 USING RECURSION 

# def print_num(n):
#     if n>5:
#         return 
#     print(n)
#     print_num(n+1)
# print_num(1)





# def demo(n):
#     if n == 0:
#         return
#     demo(n - 1)
#     print(n)
# demo(3)


# print 1213121

# def mystery(n):
#     if n == 0:
#         return
#     mystery(n-1)
#     print(n, end=" ")
#     mystery(n-1)
# mystery(3)


# print 5 4 3 2 1

# def print_num(n):
#     if n==0:
#         return 
#     print(n)
#     print_num(n-1)
# print_num(5)    



# def sun_num(n):
#     if n ==0:
#         return 0
#     return n+sun_num(n-1)
# print(sun_num(5))


# def print_num(n):
#     if n == 0:
#         return
#     print(n, end=" ")
#     print_num(n-1)
#     print(n, end=" ")
# print_num(3)    


# def fun(n):
#     if n == 0:
#         return
#     fun(n-1)
#     print(n, end="")
#     fun(n-1)
# fun(3)    


#  QUESTIONS :-

# def demo(n):

#     if n == 0:
#         return 0
#     return n + demo(n - 1)

# print(demo(3))


# def fun(n):
#     if n == 0:
#         return
#     fun(n-1)
#     print(n, end=" ")
#     fun(n-1)
# fun(3)


# def fun(n):
#     if n == 0:
#         return
#     print(n, end=" ")
#     fun(n-1)
#     print("*", end=" ")
#     fun(n-1)
# fun(2)


# def print_num(n):
#     if n==0:
#         return 0
#     return n + print_num(n-1)
# print(print_num(5))


# def fact(n):
#     if n == 0:
#         return 0
#     return n + fact(n - 1)
# print(fact(5))


# arr = [10, 20, 30, 40, 50]
# def print_array(arr, index):
#     if index == len(arr):
#         return
#     print(arr[index])
#     print_array(arr, index+1)
# print_array(arr, 0)


# arr = [10, 20, 30, 40, 50]
# def print_sum(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[0] + print_sum(arr[1:])
# print(print_sum(arr))
# print_sum(arr)


# arr = [10, 20, 30, 40, 50]
# def print_sum(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[0] + print_sum(arr[1:])
# print(print_sum(arr))
# print_sum(arr)


# num = int(input("Enter Number..."))
# if num == 0:
#     print("Zero")
# elif num >= 1:
#     print("Positive")
# else:
#     print("Negitive")     


# for i in range(1, 11):
#     if i <=10:
#         print(i)

# num = int(input('enter number..'))
# def square(n):
#     return n*n 
# print(square(num))      


# arr = [10, 20, 30, 40, 50]

# for i in arr:
#     print(i)


# arr = [5, 8, 2, 10]
# print(arr[0])


# student = {
#     "name": "Anisha",
#     "age": 20
# }
# print(student["name"])


# num = int(input("Enter number.."))
# def check(num):
#     if num % 2 == 0:
#         return("even")
#     else: 
#         return("odd")
# check(num) 
# print(check(num))     


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
            

# arr = [10, 20, 30, 40]
# sum = 0
# for i in arr:
#     sum = sum + i
# print(sum)
    

# arr = [5, 8, 2, 10, 15]
# print(len(arr))
    

# arr = [5, 8, 2, 10, 15]
# print(max(arr))


# arr = [5, 8, 2, 10, 15]
# print(min(arr))


# student = {
#     "name": "Anisha",
#     "age": 20,
#     "city": "Delhi"
# } 
# print(student["age"])


# def total(arr):
#     return sum(arr)
# arr = [10, 20, 30]
# print(total(arr))


# num = int(input("Enter Number..."))
# if num % 5 == 0:
#     print("divisible by 5")
# else:
#     print("Not divisible  by 5")    


# age = int(input("Enter age..."))
# def check(age):
#     if age >= 18:
#         print("Eligible")
#     else:
#         print("Not Eligible")
# check(age)            


# arr = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in arr:
#     if i % 2 == 0:
#         count = count + 1
# print(count)        


# student = {
#     "name": "Anisha",
#     "age": 20
# }
# student["city"] = "Delhi"
# print(student)


# arr = [8, 3, 15, 1, 10]
# print(min(arr))


# num = int(input("Enter number.."))
# def check(num):
#     if num % 2 == 0:
#         return ("even")
#     else:
#         return ("odd")
# print(check(num))    


# arr = [5, 12, 8, 20, 3, 15]
# for i in arr:
#     if i >= 10:
#         print(i)
    


# arr = [1, 2, 3, 4, 5, 6]
# sum = 0
# for i in arr:
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)        


# def largest(arr):
#     return(max(arr))
# arr = [5, 9, 2, 15, 7]
# print(largest(arr))


# arr = [5, 12, 8, 20, 3, 15]
# count = 0
# for i in arr:
#     if i < 10:
#         count = count + 1
# print(count)        


# student = {
#     "name": "Anisha",
#     "age": 20,
#     "city": "Delhi"
# }
# for key, value in student.items():
#     print(key, value)


# arr = [1, 2, 3, 4, 5, 6, 7]
# for i in arr:
#     if i % 2 != 0:
#         print(i)



# arr = [3, 10, 7, 12, 5, 18, 9] 
# sum = 0
# for i in arr:
#     if i > 8:
#         sum = sum + i
# print(sum)        


# arr = [2, 3, 6, 9, 12, 15, 4, 18]
# count = 0
# for i in arr:
#     if i % 3 == 0 and i> 5:
#         count = count + 1
# print(count)        


# arr = [4, 12, 7, 18, 21, 6, 9]
# sum = 0
# for i in arr:
#     if i % 3 == 0 and i > 10:
#         sum = sum + i
# print(sum)        


# arr = [5, 10, 15, 20, 25, 30]
# n = []
# for i in arr: 
#     if i > 15:
#         n.append(i)
# print(n)        



# arr = [3, 8, 2, 8, 5, 8, 9]  
# count = 0
# for i in arr:
#     if i == 8:
#         count = count + 1
# print(count)


# s = "programming"



# arr = [3, 7, 2, 9, 5]
# largest = arr[0]
# for i in arr:
#     if i > largest:
#         largest = i
# print(largest)        




    

# arr = [4, 1, 9, 2, 8, 3]
# smallest = arr[0]
# for i in arr:
#     if i < smallest:
#         smallest = i
# print(smallest)        





# arr = [5, 12, 7, 18, 3, 10, 15]
# count = 0
# for i in arr:
#     if i > 10 and i % 2 == 0:
#         count = count + 1
# print(count)



# arr = [2, 5, 8, 11, 14, 17, 20]
# sum = 0
# for i in range(len(arr)):
#     if i % 2 == 0:
#         sum = sum + arr[i]
# print(sum)


# arr = [6, 3, 9, 12, 5, 18, 7]
# sum = 0
# for i in arr:
#     if i % 3 == 0 and i > 6:
#         sum = sum + i
# print(sum)        



# arr = [10, 20, 5, 7, 30, 40]
# largest = arr[0]
# smallest = arr[0]

# for i in arr:
#     if i > largest:
#         smallest = largest
#         largest = i
#     elif i > smallest and i != largest:
#         smallest = i 
# print(smallest)            




# arr = [10, 20, 5, 7, 30, 40]
# largest = arr[0]
# smallest = arr[0]
# for i in arr:
#     if i > largest:
#         smallest = largest
#         largest = i
#     elif i > smallest and i != largest:
#         smallest = i
# print(smallest)            




# arr = [10, 20, 5, 7, 30, 40]
# largest = arr[0]
# smallest = arr[0]
# for i in arr:
#     if i > largest:
#         smallest = largest
#         largest = i
#     elif i > smallest and i != largest:
#         smallest = i
# print(smallest)        







# arr = [10, 20, 5, 7, 30, 40]
# largest = arr[0]
# smallest = arr[0]
# for i in arr:
#     if i > largest:
#         smallest = largest
#         largest = i
#     elif i > smallest and i != largest:
#         smallest = largest
#         smallest = i
# print(smallest)            




# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# new = []
# for i in arr:
#     if i % 2 != 0:
#         c = i*i
#         new = new + [i*i]
# print(new)        





# arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for i in arr:
#     if i % 2 == 0 or i % 3 == 0:
#         count = count + 1
# print(count)        





# word = input("enter word")
# ch = input("enter value")
# count = 0
# for i in word:
#     if i == ch:
#         count+=1
# print(count)        




# s = input("enter")
# if s == s[::-1]:
#     print("palindrom")
# else:
#     print("not")    




# s = input("enter")
# reverse = ""
# for ch in s:
#     reverse = ch + reverse
# print(reverse)







# arr = [5, 12, 7, 18, 3, 10, 15]
# largest = arr[0]
# smallest = arr[0]
# for i in arr:
#     if i> largest:
#         largest = smallest
#         smallest = i
#     elif i > smallest and i != largest:
#         largest = smallest
#         smallest = i
# print(smallest)            




# arr = [5, 12, 7, 18, 10, 15]
# sum = 0
# for i in arr:
#     sum+=i
# print(sum)



# a = "programming"
# count = 0 
# for i in a:
#     if i not in "aeiou":
#         count+=1
# print(count)    




# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print()        

# for i in range(5):
#     for j in range(i + 1):
#         print( "*", end=" ")
#     print()        



# a = "anisha"
# reverse = ""
# for ch in a:
#     reverse = ch + reverse
# print(reverse)    



# arr = [1, 2, 3, 4, 5]
# rev = []
# for i in range(len(arr)-1, -1, -1):
#     rev.append(arr[i])
# print(rev)  
#   


# s = (input("Enter..."))
# count = 0
# for ch in s:
#     count+=1
# print(count)    


# arr = [1, 2, 3, 4, 5]
# for word in arr[::-1]:
#     print(word, end=" ")





# a,b = map(int, input().split())
# if a == 0:
#     print("no")
# elif a >= b:
#     print("0")
# elif b % a == 0:
#     print("yes")
# else:
#     print("no")


# n = int(input())
# for i in range(n):
#     a = i * i
#     if a > n:
#        break
# if a == n:
#     print(i)
# else:
#     print(i-1)   

    





# a = 1
# n = int(input())
# i = 1
# def floorSqrt(n):
#     for i in range(n):
#         a = i * i
#         if a > n:
#             break;
# if a == n:
#     print(i)
# else:
#     print(i-1)
        
# floorSqrt(n)
        



# T = int(input())
# for _ in range(T):
# n = 12345
# sum = 0
# for i in n:
#     sum = sum + i
# print(sum)  





# x = 1
# result = "NNDNNDDDNNDNDN"
# carlsen = 0
# chef = 0
# for ch in result:
#     if ch == "C":
#         carlsen += 2
#     if ch == "N":
#         chef += 2
#     if ch == "D":
#         carlsen += 1
#         chef +=1
# if carlsen > chef:
#     print(60 * x)        
# elif chef > carlsen:
#     print( 40* x) 
# else:
#     print(55 * x)





# n = int(input())
# for _ in range(n):
#     score = list(map(int, input().split()))
# count = 0
# for i in score:
#     if i >= 40:
#         count += 1
#     else:
#         continue;
# print(count)    


# n = int(input())
# count = 0
# new = []
# for _ in range(n):
#     score = list(map(int, input().split()))
#     for i in score:
#         if i >= 40:
#             count +=1
#             new.append(i)
#     print(count) 
#     print(new) 


# n = int(input())
# count = 0
# max = 0
# for _ in range(n):
#     score = list(map(int, input().split()))
#     for i in score:
#         if i >= 40:
#             count +=1
#     print(count) 
  

# n = [12, 67, 45, 78, 98]
# first = 0
# second = 0
# for i in n:
#     if 







# Question 1: Check Positive, Negative, or Zero
# Problem Statement
# Take a number as input and find out whether the number is Positive, Negative, or Zero.
# Test Cases
# Test Case
# Input
# Expected Output
# 1
# 25
# Positive
# 2
# -15
# Negative
# 3
# 0
# Zero

# n = int(input())
# if n == 0:
#     print("Zero")
# elif n > 0:
#     print("Positive")
# else:
#     print("Negative")        



# Question 2: Perform Operations on Numbers from 1 to N
# Problem Statement
# Take a number n as input and check all the numbers in the range from 1 to n.
# If the number is even, subtract 10.
# If the number is odd, add 20.
# Test Cases
# Test Case
# Input (n)
# Expected Output
# 1
# 3
# 41
# 2
# 5
# 71
# 3
# 1
# 20













# Question 3: Count Positive, Negative, and Zero
# Problem Statement
# Take an array as input. Count how many numbers in the array are:
# Positive
# Negative
# Zero
# Print the count of positive numbers, negative numbers, and zeros.
# Test Cases
# Test Case
# Input Array
# Expected Output
# 1
# [10, -5, 0, 8, -2]
# Positive: 2, Negative: 2, Zero: 1
# 2
# [-1, -7, -3, 0, 0]
# Positive: 0, Negative: 3, Zero: 2
# 3
# [5, 10, 15, 20]
# Positive: 4, Negative: 0, Zero: 0



# arr = list(map(int, input().split()))
# positive = 0
# negative  = 0
# zero = 0

# for i in arr:
#     if i == 0:
#         zero += 1
#     elif i > 0:
#         positive += 1
#     else:
#         negative += 1
# print("Zero :", zero)
# print("Positive :", positive)
# print("Negative :", negative)
                




# Question 4: Convert Every Array Value to Zero
# Problem Statement
# Take an array as input and check each value of the array.
# If the number is positive, subtract 1 repeatedly until it becomes 0.
# If the number is negative, add 1 repeatedly until it becomes 0.
# If the number is already 0, keep it as 0.
# After performing the operation on every value, print the final array.
# Test Cases
# Test Case
# Input Array
# Expected Output
# 1
# [2, -3, 0]
# [0, 0, 0]
# 2
# [5, -2, 3]
# [0, 0, 0]
# 3
# [-4, 0, 1, -2]
# [0, 0, 0, 0]









# Question 1: Check Divisibility by 3
# Problem Statement

# Write a JavaScript program that takes an integer as input from the user. Determine whether the given number is divisible by 3.

# If the number is divisible by 3, print:

# Divisible by 3

# Otherwise, print:

# Not divisible by 3
# Test Cases

# Test Case 1

# Input:
# 9

# Output:
# Divisible by 3

# Test Case 2

# Input:
# 14

# Output:
# Not divisible by 3

# Test Case 3

# Input:
# 27

# Output:
# Divisible by 3


# n = int(input())
# if n % 3 == 0:
#     print("Divisible by 3")
# else:
#     print("Not divisible by 3")    







# Question 2: Check Divisibility by 3 and 7
# Problem Statement

# Write a JavaScript program that takes an integer as input and checks its divisibility.

# If the number is divisible by 3 only, print:

# three

# If the number is divisible by 7 only, print:

# seven

# If the number is divisible by both 3 and 7, print:

# both

# If the number is divisible by neither 3 nor 7, print:

# not divisible
# Test Cases

# Test Case 1

# Input:
# 6

# Output:
# three

# Test Case 2

# Input:
# 49

# Output:
# seven

# Test Case 3

# Input:
# 21

# Output:
# both

# Test Case 4

# Input:
# 10

# Output:
# not divisible


# n = int(input())
# if n % 3 == 0 and n % 7 == 0:
#     print("Both")
# elif n % 3 == 0:
#     print("Three")
# elif n % 7 == 0:
#     print("Seven")
# else:
#     print("Not Divisible")        








# Question 3: Print Numbers Divisible by 3 and/or 7 in a Range
# Problem Statement

# Write a JavaScript program that takes two integers m and n from the user, representing the starting and ending values of a range.

# Traverse all numbers from m to n (inclusive) and:

# Print the number if it is divisible by 3.
# Print the number if it is divisible by 7.
# If a number is divisible by both 3 and 7, indicate that it is divisible by both.
# Ignore all other numbers.
# Test Cases

# Test Case 1

# Input:
# m = 1
# n = 15

# Output:
# 3 -> Divisible by 3
# 6 -> Divisible by 3
# 7 -> Divisible by 7
# 9 -> Divisible by 3
# 12 -> Divisible by 3
# 14 -> Divisible by 7
# 15 -> Divisible by 3

# Test Case 2

# Input:
# m = 20
# n = 30

# Output:
# 21 -> Divisible by both
# 24 -> Divisible by 3
# 27 -> Divisible by 3
# 28 -> Divisible by 7
# 30 -> Divisible by 3

# Test Case 3

# Input:
# m = 5
# n = 10

# Output:
# 6 -> Divisible by 3
# 7 -> Divisible by 7
# 9 -> Divisible by 3




# n, m = map(int, input().split())
# for n in range(n, m):
#     if n % 3 == 0 and n % 7 == 0:
#         print("divisible by both 3, 7 = " , n) 
#     elif n % 3 == 0:
#         print("divisible by 3 = " , n )
#     elif n % 7 == 0:
#         print("divisible by 7 = " , n)   






# Question 4: Filter Array Elements
# Problem Statement

# Write a JavaScript program that takes an array of integers.

# Print only those elements that are:

# Divisible by 3, or
# Divisible by 7

# However:

# Do not print numbers that are divisible by both 3 and 7.
# Do not print numbers that are divisible by neither 3 nor 7.
# Test Cases

# Test Case 1

# Input:
# [3, 6, 7, 9, 14, 21, 28, 35]

# Output:
# 3
# 6
# 7
# 9
# 14
# 28
# 35

# Test Case 2

# Input:
# [10, 12, 18, 21, 25, 42]

# Output:
# 12
# 18

# Test Case 3

# Input:
# [1, 2, 4, 5, 8]

# Output:
# No valid numbers found.


# newarr = []
# arr = list(map(int, input().split()))
# for i in arr:
#     if i % 3 == 0 or i % 7 == 0:
#         newarr.append(i)
# print(newarr)        


# Question 1: Write a program that asks the user to input a single integer. 
# Use an if-else statement to check if the last digit of the number is equal to 9.
# If it is, print: "The number ends with 9."
# If it is not, print: "The number does not end with 9..

# n = int(input())
# if n%10 == 9 or n == 9:
#     print("The number ends with 9.")
# else:
#     print("The number does not end with 9")    





# Question 2: Write a program that takes an integer input from the user. 
# The user might enter a negative number (e.g., -149).
# First, write logic to ensure the number is treated as positive (convert it if necessary).
# Then, use an if-else block to check if the last digit is 9.
# Print "Valid 9-ender" if it ends in 9, and "Invalid" otherwise.

# n = int(input())
# if n%10 == 9:
#     print("Valid 9-ender")
# else:
#     print("Invalid")  



# Question 3: Write a program that uses a while loop to 
# continuously ask the user to enter a number.
# If the user enters a number that does not end in 9, 
# the loop should print "Try again!" and ask for another number.
# If the user enters a number that does end in 9, 
# the loop should print "You found the magic number!" and terminate (break).


# n = int(input())
# while n > 0:
#     if n % 10 == 9:
#         print("You found the magic number!")
#         break
#     else:
#         print("Try again!")
#         n = int(input())
        
    



# Question 4:
# Write a program that uses a for loop to ask the user to input exactly 5 different integers, one by one.
# Inside the loop, use an if statement to check if the current number ends in 9.
# Keep a running count of how many numbers end in 9.
# After the loop finishes, use an if-else statement on the final count: if the count is greater than 0,
# print "You entered [count] numbers ending in 9." Otherwise, print "No numbers ended in 9."

# count = 0
# for _ in range(5):
#     n = int(input())
#     if n % 10 == 9:
#         count += 1
# print("You entered ",count, "numbers ending in 9")        




# Question 5: 
# Write a program that asks the user to input 10 integers and stores them in an array (or list).
# Once the array is populated, use a loop to iterate through the entire array.
# Use an if condition to find every number whose last digit is 9 and append those specific numbers into a new, separate array.
# Finally, print the original array and the new filtered array. If the new array is empty, 
# print "No numbers ending in 9 were found in the dataset."



# A company has N employees. Each employee has completed a certain number of tasks.
# An employee is eligible for a bonus if:
# Tasks completed ≥ 50
# AND tasks completed is an even number.
# Print the number of eligible employees.


# count = 0
# n = int(input())
# newarr = []
# task = list(map(int, input().split()))
# for i in task:
#     if i >= 50 and i % 2 == 0:
#         count += 1
#         newarr.append(i)
# print("Count of eligible employees for bonus", count)        
# print(newarr)



# count = 0
# n = int(input())
# newarr = []
# highest = 0
# second_highest = 0
# promoted_employee = 0
# task = list(map(int, input().split()))
# for i in task:
#     if i >= 50 and i % 2 == 0:
#         count += 1
#         newarr.append(i)
#         for a in newarr:
#             if a > highest:
#                 second_highest = highest
#                 highest = a
#             elif a > second_highest and a != highest:
#                second_highest = a
# promoted = 90/ 100 * highest               
# for j in newarr:
#     promoted = 90/ 100 * highest
#     if j >= promoted:
#         promoted_employee += 1   
         
# print("Count of eligible employees for bonus", count)        
# print(newarr)
# print("Highest", highest)
# print("Second Highest",second_highest)
# print("promoted employee count = ", promoted_employee)







# count = 0
# n = int(input())
# newarr = []
# task = list(map(int, input().split()))
# for i in task:
#     if i >= 50 and i % 2 == 0:
#         count += 1
#         newarr.append(i)
#         for a in newarr:
            

# print("Count of eligible employees for bonus", count)        
# print(newarr)







# There are 5 products.
# Create two arrays:
# One array stores the MRP.
# Another array stores the Discount Percentage.
# Using arrays:
# Calculate the selling price of every product.
# Display the selling price.
# Test Case
# Product
# MRP
# Discount
# 1
# 100
# 10
# 2
# 200
# 15
# 3
# 150
# 20
# 4
# 80
# 5
# 5
# 300
# 25





# price = list(map(int, input().split()))
# discount = list(map(int, input().split()))

# for i in price:
#     for j in discount:
#         c = int(j/100*i)
#         print(c)



# Problem:
# Store the MRP and Discount of 6 products in arrays.
# For every product:
# If the discount is between 0 and 100, calculate the selling price.


# Otherwise print "Invalid Discount".

# mrp = list(map(int, input().split()))
# dis = list(map(int, input().split()))

# for i,j in zip(mrp, dis):
#         if j > 0 and j <=100:
#             dis = int(i/100*j)
#             sp = i-dis
#             print(sp)
#         else:
#             print("Invalid Discount")    





# Problem 1:
# Write a Python program to take Cost Price (C.P.) and Selling Price (S.P.) as input.

# If S.P. is greater than C.P., calculate and print Profit Percentage.
# Otherwise, print "Invalid".
# Test Cases
# C.P.    S.P.    Expected Output
# 100    120    Profit Percentage = 20%
# 300    250    Invalid


# cp = int(input())
# sp = int(input())
# if sp > cp:
#     profit = sp - cp
#     print(profit)
# else:
#     print("Invalid")    




# Multiple Products

# Problem:
# A shopkeeper has information about 5 products.

# For each product, take C.P. and S.P. as input.

# If S.P. is greater than C.P., calculate Profit Percentage.
# Otherwise, print "Invalid".

# Condition: Do not use a loop.

# Test Cases
# Product    C.P.    S.P.    Expected Output
# Product 1    100    150    50%
# Product 2    400    300    Invalid


# cp = int(input())
# sp = int(input())
# if sp > cp:
#     profit = sp - cp
#     print(profit)
# else:
#     print("Invalid")    



# cp = int(input())
# sp = int(input())
# if sp > cp:
#     profit = sp - cp
#     print(profit)
# else:
#     print("Invalid")  



# cp = int(input())
# sp = int(input())
# if sp > cp:
#     profit = sp - cp
#     print(profit)
# else:
#     print("Invalid")  



# cp = int(input())
# sp = int(input())
# if sp > cp:
#     profit = sp - cp
#     print(profit)
# else:
#     print("Invalid")  



# cp = int(input())
# sp = int(input())
# if sp > cp:
#     profit = sp - cp
#     print(profit)
# else:
#     print("Invalid")         



# 3.  Single Loop

# Problem:
# Write a Python program that takes C.P. and S.P. for 5 products using a loop.

# For every product:

# Check whether S.P. is greater than C.P.
# If yes, calculate Profit Percentage.
# Otherwise, print "Invalid".

# Condition: Use only one loop.

# Test Cases
# Product    C.P.    S.P.    Expected Output
# 1    200    240    20%
# 2    500    400    Invalid




# for i in range(2):
#     cp = (input())
#     sp = (input())

# if sp > cp:
#     profit = sp - cp
#     print(profit)
# else:
#     print("Invalid")  








# Ques1
# Write a Python program that takes a number as input and prints its square.
# Input: 7
# Output: 49

# n = int(input())
# print(n*n)



# Ques2
# Write a Python program that takes a number as input and calculates and prints its square root.
# Input: 81
# Output: 9

# n = int(input())
# for i in range(n/2):
    # a = i*i
    # if a==n:
    #     print(i)
    # else:
    #     print("invalid")
    #     break



# Write a Python program that takes a list of integers and prints the sum of squares of all even numbers in the list.
# Input: [1, 2, 3, 4, 5, 6]
# Output: 56   (2² + 4² + 6² = 4+16+36)

# n = list(map(int, input().split()))
# s = 0
# for i in n:
#     if i % 2 == 0:
#         a = i*i
#         s = s + a
# print(s)    




# Write a Python program that takes a list of positive integers and prints the square root of the largest perfect square present in the list. Ignore numbers that are not perfect squares.
# Input:
# [16, 25, 10, 49, 30, 81, 17]
# Output:
# 9

# n = list(map(int, input().split()))
# sq = 0
# for i in n:
#     for j in range(1, i):
#         a = j * j
#         if a==i and sq <= j:
#             sq = j
#             break      
# print(sq) 




# Q1 Login Attempt Monitor 🔐
# A system logs login attempts as a list of 
# "Success" / "Fail" strings for one user. If a user
#  has 3 consecutive failed attempts, the account should be 
# locked immediately at that point, print the index where it got locked.
#  If it never happens, print "Account Safe".

# Input: ["Success", "Fail", "Fail", "Success", "Fail", "Fail", "Fail"]
# Output: Account locked at index 6

# Constraint: You cannot use .count(). Use loop.

# arr = input().split()
# count = 0

# for i in range(len(arr)):
#     if  arr[i] == "fail":
#         count +=1
#         if count >= 3:
#             print("Account locked at index", i)
#             break
#     else:
#         count = 0
# else: 
#     print("Account Safe")     




# A company has 2 branches, each branch has 2 departments, and each department has 3 workers. Take the age, gender, and working days of every worker and calculate their wages.

# Input:
# Branch 1:
# Department 1 → [20, "M", 10], [25, "F", 10], [30, "M", 10]
# Department 2 → [35, "F", 10], [22, "M", 5], [40, "F", 6]
# Branch 2:
# Department 1 → [28, "F", 7], [32, "M", 9], [17, "M", 10]
# Department 2 → [19, "F", 6], [31, "M", 10], [26, "M", 7]

# Output:
# Branch 1
# Department 1 → ₹7000, ₹7500, ₹8000
# Department 2 → ₹8500, ₹3500, ₹5100
# Branch 2
# Department 1 → ₹5250, ₹7200, Enter appropriate age
# Department 2 → ₹4500, ₹8000, ₹4900
# Constraint: Use three nested loops.


# for _ in range(2):
#     branch = int(input("branch "))
#     for _ in range(2):
#         dep = int(input("dep "))
#         for _ in range(3):
#             age = int(input("age "))
#             gender = str(input("gender "))
#             days = int(input("days "))
#             if age >= 18 and age <= 40:
#                 if gender == "F":
#                     print(days * 750)
#                 else:
#                     print(days * 700)   
#             else:
#                 print('Enter valid age')         






 	
# Given three 1D arrays containing age, gender, and working days of 5 workers, calculate the wage of each worker.
# age = [20, 25, 30, 40, 17]
# gender = ["M", "F", "M", "F", "M"]
# days = [10, 10, 10, 10, 10]

# Output:
# ₹7000
# ₹7500
# ₹8000
# ₹8500
# Enter appropriate age
# Constraint: Use loops. Do not create separate wage values manually.



# age = list(map(int, input("age= ").split()))
# gender = list(map(str, input("gender= ").split()))
# days = list(map(int, input("days= ").split()))
# for i, k, j in zip (age, gender, days):
#     if i >= 18 and i <= 40:
#         if k == "M":
#             print(j * 700)        
#         else:
#             wages = j * 750
#             print(wages)  
#     else:
#         print("enter valid age")


                    



 	
# A company has 3 departments, with 3 workers in each department. Store each worker's age, gender, and working days in a 2D array and calculate their wages.

# arr = [
#   [[20,"M",10], [25,"F",10], [30,"M",10]],
#   [[35,"F",10], [22,"M",5], [40,"F",6]],
#   [[28,"F",7], [32,"M",9], [17,"M",10]]
# ]

# Output:

# Department 1 → ₹7000, ₹7500, ₹8000
# Department 2 → ₹8500, ₹3500, ₹5100
# Department 3 → ₹5250, ₹7200, Enter appropriate age\







# rh = int(input())
# cc = float(input())
# ts = int(input())

# if rh > 50 and cc > 0.7 and ts > 5600:
#     print("Grade 10")
# elif rh > 50 and cc > 0.7 and ts < 5600:
#     print("Grade 9")
# elif rh < 50 and cc > 0.7 and ts > 5600:
#     print("Grade 8") 
# elif rh > 50 and cc < 0.7 and ts > 5600:
#     print("Grade 7")   
# else:
#     print("Grade 0")        
# 
    



# for _ in range(2):
#     rh = int(input())
#     cc = float(input())
#     ts = int(input())
#     if rh > 50 and cc > 0.7 and ts > 5600:
#         print("Grade 10")
#     elif rh > 50 and cc > 0.7 and ts < 5600:
#         print("Grade 9")
#     elif rh < 50 and cc > 0.7 and ts > 5600:
#         print("Grade 8") 
#     elif rh > 50 and cc < 0.7 and ts > 5600:
#         print("Grade 7")   
#     else:
#         print("Grade 0")  





 
 	
# Ques1: Write a Python program that takes a number n and prints a square pattern of * with n rows and n columns.

# Input: 4
# Output:
# ****
# ****
# ****
# ****
# n = int(input())
# for i in range(n):
#         print("*" * n)



# Ques2: Write a Python program that takes a number n and 
# prints a right-angled triangle pattern.

# Input: 5
# Output:
# *
# **
# ***
# ****
# *****

# n = int(input())
# for i in range(n+1):
#     print("*" * i)
        

            

 	
# Ques3: Write a Python program that takes a number n and 
# prints the following number pattern using nested loops.

# Input: 5
# Output:
# 1
# 12
# 123
# 1234
# 12345

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
            
            


 	
# 1. Find User with Highest Balance
# You are given an array of user records stored in memory.
# const users = [
#   { id: 1, name: "Rinki", balance: 4500 },
#   { id: 2, name: "Amit", balance: 12000 },
#   { id: 3, name: "Neha", balance: 8000 }
# ];
# Find the user who has the highest account balance.
# Expected Output
# Amit - ₹12000







# arr = []
# id = list(map(int, input().split()))
# j = 1
# for i in id:      
#         if i == j:
#             j+=1
#         else:    
#             arr.append(j)
#             j += 2
# print(arr)            






# id = list(map(int, input().split()))
# name = list(map(str, input().split()))
# balance = list(map(int, input().split()))
# highest = 0
# for i in balance:
#     if highest > i:
#         highest = highest
#     else:
#         highest = i    
# index = balance.index(highest)
# print(name[index])
# print(highest)
 




 	
# 2. Merge Two Database Tables
# You have two collections.
# Users
# [
#   { id: 1, name: "Rinki" },
#   { id: 2, name: "Amit" }
# ]
# Orders
# [
#   { userId: 1, product: "Laptop" },
#   { userId: 2, product: "Mouse" },
#   { userId: 1, product: "Keyboard" }
# ]
# Merge them so each order also contains the user's name.
# Expected Output
# [
#   { name: "Rinki", product: "Laptop" },
#   { name: "Amit", product: "Mouse" },
#   { name: "Rinki", product: "Keyboard" }
# ]





 	
# 2. Reverse Username
# Input:
# Rinki
# Output:
# ikniR



# s = input("enter")
# reverse = ""
# for ch in s:
#     reverse = ch + reverse
# print(reverse)


# word = str(input())
# print(word.capitalize())


# files = input().split()
# result = {}
# for i in files:
#     ext = i.split(".")[1]
#     if ext in result:
#         result[ext] +=1
#     else:
#         result[ext] = 1
# print(result)           




# a = list(map(int, input().split()))
# count = 0
# for i in a:
#     for j in a:
#         if i == j:
#             count +=1
#         else:
#             continue
# print(count)        
                






# * * * * *
# * * * *
# * * *
# * *
# *



# n = int(input())
# for i in range(n):
#     if i >0:
#         for j in range(n):
#             if j < n:
#                 print("*", end=" ")
#                 j+=1
#                 continue
# i-=1                







#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# n = int(input())
# for i in range(1, n+1):

#     for j in range(n-i):
#         print("  ", end="")

#     for j in range(i):
#         print("* ", end="")

#     print()    








# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# n = int(input())
# for i in range():
#     print("*")

  





# Q1: Find the Key with the Maximum Value
# Given a dictionary of item names and their prices, find 
# which key has the highest value. 
# INPUT: {"apple": 30, "banana": 50, "mango": 45}
# OUTPUT: "banana"







 
 	
# Q3: Find Both Min and Max (Multiple Return Values)
# Write a function that returns both the smallest and the 
# largest number in a list at once.
# INPUT: [4, 2, 9, 1, 7]
# OUTPUT: (1, 9) 


# arr = list(map(int, input().split()))
# print(min(arr), max(arr))






 
 	
# Sort 0s and 1s
# Input
# 8
# 0 1 1 0 1 0 0 1
# Output
# 0 0 0 0 1 1 1 1

# a = list(map(int, input().split()))
# print(a.sort)





# n = str(input().split())
# x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# count = 0
# for i in n:
#     for j  in x:
#         if i == j:
#             count +=1
#         else:
#             continue    
# print(count)        






# a = list(map(str, input().split()))
# x = "AEIOUaeiou"
# count = 0
# for i in a:
#     for j in x:
#         if i[0] == j:
#             count += 1
#         else:
#             continue
# print(count)            





#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# n = int(input())
# for i in range(1, n+1):
#     space = n-i
#     star = 2 *i -1
#     print(" " * space + "*" * star)
# for i in range(n-1,0, -1):
#     space = n-i
#     star = 2 *i -1
#     print(" "* space + "*" * star)    







# n = int(input())
# if n <= 5:
#     print(n*2)
# elif n <= 10:
#     print(n*3)
# elif n <= 15:
#     print(n*4)
# else:
#     print(n*5)            
   



# n = list(map(int, input().split()))
# largest = 0
# for i in n:
#     if i > largest:
#         largest = i
# index = n.index(largest)
# print(index, largest)







# Input: [1, 2, -3, -1, 4, -5]
# Output: [1, -3, 2, -1, 4, -5]

# n = list(map(int, input().split()))
# positive = []
# negitive = []
# arr = []
# for i in n:
#     if i> 0:
#         positive.append(i)
#     else:
#         negitive.append(i)    










# Input: [1, 2, 3, 4]           
# Output: [24, 12, 8, 6]

# n = list(map(int, input().split()))
# arr = []
# for i in n:
#     new = 1
#     for j in n:
#         index1= n.index(i)
#         index2 = n.index(j)
#         if i != j and index1 != index2:
#                 new = j * new
#     arr.append(new)
# print(arr)            











# Q2: Vowel Counter per Word 🔤
# Given a sentence, split it into words manually and 
# count the number of vowels in each word.
# INPUT: "the quick brown fox"
# OUTPUT: [('the', 1), ('quick', 2), ('brown', 1), ('fox', 1)]


# n = list(map(str, input().split()))
# a = "AEIOUaeiou"
# for i in n:
#     count = 0
#     for j in i:
#         for k in a:
#             if j == k:
#                 count += 1
#     print(i, count)




# n = int(input())
# for i in range(n):
#         for j in range(n):
#             if j % 2 == 0:
#                 print("#", end=" ")
#             else:
#                 print(".", end=" ") 
    # else:
    #     for j in range(n):
    #         if j % 2 != 0:
    #             print("#", end=" ")
    #         else:
    #             print(".", end=" ")                         
 


# n = int(input())
# for i in range(n):
#     if i % 2 != 0:
#                 print(".", end=(" "))
#     else:
#                 print("#", end=(""))     

#     for j in range(n):
#             if j % 2 == 0:
#                 print("#", end="")
#             else:
#                 print(".", end="")   
          

    


# n = int(input())
# for i in range(n):
#     print("*"* n)





# n = list(map(int, input().split()))
# post = 0
# negi = 0
# zero = 0

# for i in n:
#     if i > 0:
#          post += 1    
#     elif i == 0:
#           zero +=1
#     else:
#          negi +=1

# print("zero:",zero ,
# "post:",post, "negative:",negi)






# key = input().split()
# value = list(map(int, input().split()))
# obj = {}

# print(key)
# print(value)



# n = {}
# a = {}

# for i in range(3):
#     key = input()
#     value = int(input())
#     n[key] = value

#     for j in n:
#         value = n[j]
#         a[value] = j
# print(a)   





# n = list(map(int, input().split()))
# highest = 0
# for i in n:
#     if i > highest:
#         highest = i
# print(highest)


# n = list(map(int, input().split()))
# smallest = n[0]
# for i in n:
#     if i < smallest:
#         smallest = i
# print(smallest)


# n = list(map(int, input().split()))
# count = 0
# for i in n:
#     if i >= 60:
#         count += 1
# print(count)


# n = list(map(int, input().split()))
# count = 0
# sum = 0
# for i in n:
#     if i >= 60:
#         count += 1
# print(count)





# n = list(map(int, input().split()))
# even_sum = 0
# odd_sum = 0
# for i in n:
#     if i % 2 == 0:
#         even_sum = i + even_sum
#     else:
#         odd_sum = i + odd_sum
  
# print(even_sum)
# print(odd_sum)         
# print(even_sum - odd_sum)

# if even_sum >= odd_sum:    
#     print("Even")
# else:
#     print("Odd")  







# seats = list(map(str, input().split()))
# for i in seats:
    

# seats = input().split()
# sum = 0
# count = 0
# for i in seats:
#     row = i[0]
#     if row == "A":
#         count += 1
#     num = int(i[1:]) 
#     sum += num
#     print(row ,"->",num)
# print(count)
# print(sum)        



 	
# 1 2 3 4 5
# 5 4 3 2 1
# 1 2 3 4 5
# 5 4 3 2 1

# n = int(input())
# for i in range(n):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()   

#     for j in range(5, 0 , -1):
#         print(j, end=" ")
#     print()     
        
   

# amount = int(input())
# if amount < 1000:
#     print(amount)
# elif amount <= 4999:
#     discount = 5/100*amount
#     profit = amount-discount
#     print(int(profit))
# elif amount <= 9999:
#     discount = 10/100*amount
#     profit = amount-discount
#     print(int(profit))
# else:
#     discount = 15/100*amount
#     profit = amount-discount
#     print(int(profit))




 
 	
# Ques6: Write a Python program that takes a list of integers and finds the second largest unique number without using sort() or max().

# Input: [10, 5, 20, 8, 20, 15]
# Output: 15

# n = list(map(int, input().split()))
# highest = 0
# second = 0

# for i in n:
#     if i > highest:
#         second = highest
#         highest = i
#     else:
#         i > second and i !=highest
#         second = i
# print(second)        




# n = list(map(int, input(). split()))
# dot = 0
# for i in n:
#     if i == 0:
#         dot += 1
# print("Dot Balls = ",dot)        
# sum = 0
# for i in n:
#     sum = sum + i
# print("Total Score = ",sum)    
# count = 0
# for i in n:
#     if i == 4 or i == 6:
#         count += 1
# print("Boundaries = ",count)        



# n = 1234
# sum = 0
# for i in n:
#     sum = sum + 1
# print(sum)    




# n, m, k = map(int, input().split())
# for _ in range(m):
#     a = list(map(int, input().split()))
#     for i in range(1, n+ 1):
#         if i not in a:
#             print(i)
    
    



# t = int(input())
# for  _ in range(t):
# count = 0
# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))
# for i in range(1, n+1):
#         if i not in a:
#             count += 1
#             if count <= k: 
#                 print(i, end=" ")
#             else:
#                  continue    

                    




