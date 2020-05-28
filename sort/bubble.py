#!/usr/bin/python
#coding=utf-8


#冒泡排序

#从小到大 n个数
#i = 0 最开始两个数比较，如果第一个数大于第二个数，就交换两个数，然后比较第二、三个数，类推比较n-1次，最大数在最后，总共比较n-1次
#i = 1 然后从新开始比较，直到倒数第二个数，结束这一轮，这样，最后两个数就是按循序排列了， 总共比较 n-1-1次
#i = n - 2 总计进行n-1次排序(注意i从0开始，i=n-2 即 第n-1次排序)，整个数组排序完成   每次比较 n-1-i 次
#时间复杂度计算: 
#遍历次数
# (n-1) + (n-2) + ... + 1 = ((n-1) + 1 ) * (n-1)/2 = n * (n-1)/2 = (n^2 - n)*0.5
# 当n比较大时  (n^2 - n)*0.5 ≈ n^2 * 0.5  ,
# 即时间复杂度O(n^2)表示数量级，忽略系数0.5

import tools
import copy

kCount = 0 #统计循环次数

def maxCount(n):
	return n*(n-1)*0.5

#测试一次排序
def handle(n):
	list = tools.createArray(n)  #随机生成n个数
	print '生成数组',list
	return sort3(list)

#同一算法，多次数据测试
def moreHanle(count,n):
	global kCount
	for i in range(count):
		kCount = 0
		list = handle(n)
		# print '完成排序',list
		if kCount > maxCount(n):
			print '排序次数异常',list,kCount
		elif kCount < maxCount(n):
			print '排序得到优化',list,kCount
		else:
			print '正常排序',list,kCount
		print '-----------------------------------------------------'

#同一数据，不同算法测试
def moreSortHandle(count,n):
	global kCount
	for i in range(count):
		list = tools.createArray(n)  #随机生成n个数
		print '生成数组',list
		kCount = 0
		sort(copy.copy(list))
		print 'sort',kCount
		kCount = 0
		sort1(copy.copy(list))
		print 'sort1',kCount
		kCount = 0
		sort2(copy.copy(list))
		print 'sort2',kCount
		kCount = 0
		sort3(copy.copy(list))
		print 'sort3',kCount
		print '-----------------------------------------------------'


#基本排序
def sort(list):
	global kCount #标记全局变量，才能修改
	n = len(list)
	for i in range(n-1): #python 实现索引遍历 , 遍历n-1次
		for j in range(n-1-i): # 每次只需要遍历n-1-i 次，因为每次的最后i个数，是排好序的，不要再比较
			kCount = kCount + 1
			if list[j] > list[j+1]:
				tools.swap(list,j,j+1)
	return list

#优化方案1
#如果数组经过几次交换后，已经完成所有顺序排列，则后续的遍历，则无意义
def sort1(list):
	global kCount #标记全局变量，才能修改
	n = len(list)
	for i in range(n-1): #python 实现索引遍历 , 遍历n-1次
		flag = -1 #记录每次遍历是否发生交换
		for j in range(n-1-i): # 每次只需要遍历n-1-i 次，因为每次的最后i个数，是排好序的，不要再比较
			kCount = kCount + 1
			if list[j] > list[j+1]:
				tools.swap(list,j,j+1)
				flag = 1
		if flag == -1: #一次循环结束，没有发生交换，说明，数组是顺序是好的，不需要再排
			return list

	return list

#优化2
#优化1.仅仅适用于连片有序而整体无序的数据(例如：1， 2，3 ，4 ，7，6，5)。
#对于 前面大部分无序，而后边小半部分有序，排序效率不高[1,2,5,7,4,3,6,8,9,10]
#因此我们记录最后一次交换的位置，后边没有交换，必然有序，然后下一次排序从第一个到记录的位置结束即可
# [1, 2, 5, 7, 4, 3, 6, 8, 9, 10] 
# [1, 2, 5, 4, 3, 6, 7, 8, 9, 10] 最后交换位置：6
# [1, 2, 4, 3, 5, 6, 7, 8, 9, 10] 最后交换位置：4
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 最后交换位置：3
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 无交换

#有很大提升
def sort2(list):
	global kCount #标记全局变量，才能修改
	n = len(list)
	k = n - 1 #用于内循环次数
	pos = 0 #记录最后交换位置
	for i in range(n-1): 
		flag = -1 #记录每次遍历是否发生交换
		for j in range(k): #遍历到上次交换的位置
			kCount = kCount + 1
			if list[j] > list[j+1]:
				tools.swap(list,j,j+1)
				flag = 1
				pos = j
		#print list
		if flag == -1: #说明在第一个位置交换了，即全部排序完成
			return list
		k = pos

	return list

#优化3
#虽然2，已经提升很大，但还有一种优化,利用一次循环，可以确定两个值，一个最大值，和一个最小值
#正向确定最大值，反向确定最小值
def sort3(list):
	global kCount #标记全局变量，才能修改
	n = len(list)
	k = n - 1 #用于内循环次数
	pos = 0 #记录最后交换位置
	h = 0 #同时找最大值，最小值，需要两个下标遍历
	for i in range(n-1): 
		flag = -1 #记录每次遍历是否发生交换

		#正向查找最大值
		for j in range(h,k): #遍历到上次交换的位置
			kCount = kCount + 1
			if list[j] > list[j+1]:
				tools.swap(list,j,j+1)
				flag = 1
				pos = j

			# print '++',list,kCount


		# print '正向结束',list,kCount
		if flag == -1: #说明在第一个位置交换了，即全部排序完成
			return list

		k = pos

		#反向查找最大值
		flag = -1
		for x in range(k,h,-1):
			kCount = kCount + 1
			if list[x] < list[x-1]:
				tools.swap(list,x,x-1)
				flag = 1
				h = x
			# print '--',list,kCount
		# print '反向结束',list,kCount

		if flag == -1: #说明在第一个位置交换了，即全部排序完成
			return list



	return list

if __name__ == "__main__":
	# print sort([5, 12, 15, 11, 25, 20])
	# print sort1([5, 12, 15, 11, 25, 20])
	# print sort2([5, 12, 15, 11, 25, 20])
	# print sort3([5, 12, 15, 11, 25, 20])

	# print sort2([31, 24, 8, 30, 10, 5])
	# print sort2([6, 6, 2, 2, 1, 1])
	# print sort3([31, 24, 8, 30, 10, 5])
	# print handle(6)
	print '循环次数',kCount
	# moreHanle(100,6)
	moreSortHandle(100,100)


