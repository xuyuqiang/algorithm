#!/usr/bin/python
#coding=utf-8

import random

#创建数组
def createArray(n):
	if not isinstance(n,int):
		print "n not is int"
		return []
	list = []
	i = 0
	while i < n:
		list.append(random.randint(0, n*n))
		i = i + 1
	return list


#交换两个数，这里为了实现更多的方法交换的方法
#因为python中不能选择引用传递参数，故选择这种方式定义参数

#1.利用临时变量
def swap(list,i,j): 
	temp = list[i]
	list[i] = list[j]
	list[j] = temp



if __name__ == '__main__':
	print createArray(6)
	