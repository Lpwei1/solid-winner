# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# lis=[56,12,1,8,454,10,100,34,56,7,23,456,234,-58]
# # print(len(lis))
# def sortport():
#     for i in range(len(lis)-1):
#         for j in range(len(lis)-1-i):
#             if lis[j]>lis[j+1]:
#                 lis[j],lis[j+1]=lis[j+1],lis[j]
#     return lis
# a=sortport()
# print(a)

# def power(x,n):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# a=power(3,2)
# print(a)
# def calc(numbers):
#     sum=0
#     for n in range(numbers):
#         sum=sum+n*n
#     return sum
# a=calc(3)
# print(a)

# def fac():
#     num=int(input("请输入一个数字："))
#     factorial=1
#     if num<0:
#         print('抱歉，负数没有阶乘')
#     elif num==0:
#         print('0的阶乘为1')
#     else:
#         for i in range(1,num+1):
#             factorial=factorial*i
#         print("%d的阶乘为%d" %(num,factorial))
#         return factorial
# a=fac()
# print(a)

# L=['Hello','World','IBM','Apple']
# LL=str(L)
# print(LL.lower())
# LLL=list(LL)
# print(type(LLL))
# import os
# def print_dir():
#     filepath=input('请输入一个路径：')
#     if filepath=='':
#         print('请输入正确的路径')
#     else:
#         for i in os.listdir(filepath):
#           print(os.path.join(filepath,i))
# print_dir()
# L=['James','Meng','Xin']
# for i in range(len(L)):
#     print('Hello,%s' %L[i])
# list1=[2,3,8,4,9,5,6]
# list2=[5,6,10,17,11,2]
# list3=list1+list2
# print(list3)
# print(set(list3))
# import logging          
# logging.basicConfig(level=logging.INFO)
# s='1'
# n=int(s)
# nn=n+1
# logging.info('n=%d' %n)
# print (10/n)
# a=list(range(0,20))
# import numpy as np
# my_list=np.array(range(5))
# my_list*5
list(range(5,1))