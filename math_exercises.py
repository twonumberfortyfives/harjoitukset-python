# h = int(input("z = "))
# x = int(input("x = "))
# def numero(z):
#     return z - x
# print(numero(x))

# def numero(luku):
#         return luku - x
# numero(100)
# y = numero(100)
# b =  abs(y)
# _____________________________ex2
# def max_sum(A):
#     x = 0
#     for i in A:
#         x += int(i)
#     return x / len(A)
#  
#  
# try:
#     A = input("numbers: ").split()
#     print(max_sum(A))
#  
# except ValueError:
#     print("Input error")
# _____________________________ex1
# x = int(input("x = "))
# y = int(input("y = "))
# def numbers(x, y):
# 
#     print(x + y)
# numbers(x, y)
#_____________________________ex2 (second variant)
# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# def numbers(x, y, z):
#     print((x + y + z)/3)
# numbers(x,y,z)



#____________________________without def ex 3
# guys = [12,32,4,12]
# for i in range(len(guys)):
#     if guys[i] % 2== 0:
#         print("yes")
#     else:
#         print("no")
#_____________________________with def ex 3
# def my_function(food):
#     for i in food:
#         if i % 2 == 0:
#             print(i)
#     
# fruits = [3, 6, 2]
# my_function(fruits)
#________________________ ex 4
# def my_function(food):
#     for i in food:
#         if i % 2 > 0:
#             print(i)
#      
# fruits = [3, 6, 2]
# my_function(fruits)
# ____________________________ ex 5
# z = int(input("z = "))
# def numbers (z):
#     print(z + 1)
# numbers(z)
# ___________________ ex 6
# b = int(input("b = "))
# def numbers (b):
#     print(abs(b))   
# numbers(b)
# _______________________ ex 7 (maximum)
# def large(arr): 
#     maxss_ = arr[0]
#     for ele in arr:
#         if ele > maxss_:
#            maxss_ = ele
#     return maxss_ 
# 
# 
# list1 = [1,4,5,2,6]
# result = large(list1)
# print(result)

#  _______________________ ex 7 (minimum)
# def large(arr): 
#     maxss_ = arr[0]
#     for ele in arr:
#         if ele < maxss_:
#            maxss_ = ele
#     return maxss_ 
# 
# 
# list1 = [1,4,5,2,6]
# result = large(list1)
# print(result)
# _________________________ middle ex 7
# def calc_average(lst):
#     return sum(lst) / len(lst) 
# lst = [24, 19, 35, 46, 75, 29, 30, 18] 
# average = calc_average(lst)
# print("middle ", round(average, 3)) 

# ___________________________ ex  8
# def pupsik(hole):
#     if hole <= 1:
#         return hole
#     else:
#         return (pupsik(hole - 1) + pupsik(hole - 2))
#     
# nhuey = 21
# for i in range(nhuey):
#     print(pupsik(i))
#     
