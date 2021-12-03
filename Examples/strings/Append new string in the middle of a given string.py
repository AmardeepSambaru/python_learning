# Given two strings, s1 and s2.
# Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = input("enter the name 1 :")
s2 = input("enter the name 2 :")
s1_len = len(s1)
#first = s1[:midd_s1]
midd_s1 = int(s1_len / 2)
last = s1[midd_s1:]
print(s1[:midd_s1] + s2 + last)

