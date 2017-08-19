# a = range(10)
# b = sum(a)
# print b
#
#
# a = [1,2,3]
# print max(a)
#
# a = [1,2,3]
# print min(a)
#
# a = range(2,10,2)
# print a

# def pos_num():
#     my_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     for i in range(len(my_list)):
#         if my_list[i] > 0:
#             print my_list[i]
#
# pos_num()

# def pos_num_2():
#     my_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     new_list = []
#
#     for i in range(len(my_list)):
#         if my_list[i] > 0:
#             new_list.insert(i, my_list[i])
#
#     print new_list
#
# pos_num_2()

# def multiplyList():
# 	my_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	factor = 10
# 	new_list = []
#
# 	for i in range(len(my_list)):
# 	    new_list.insert(i, my_list[i] * factor)
#
# 	print new_list
# multiplyList()

#
# def multVect():
#
# 	list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	new_list = []
#
# 	for i in range(len(list_1)):
# 	    new_list.insert(i, list_1[i] * list_2[i])
#
# 	print "list one: "
# 	print list_1
# 	print "list two: "
# 	print list_2
# 	print "product: "
# 	print new_list
#
# multVect()

# def matAdd():
#
# 	list_1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# 	            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
# 	list_2 = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
# 	            [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]]
# 	product = [[],[]]
#
# 	for i in range(len(list_1)):
# 	    for x in range(len(list_1[i])):
# 	        product[i].append(list_1[i][x] + list_2[i][x])
#
# 	print product
#
# 	list_1 = ['apples', 'apples', 'bananas', 'bananas', 'pears', 'bananas']
# 	list_2 = []
#
# 	for i in list_1:
# 	    if i not in list_2:
# 	        list_2.append(i)
#
# 	print list_1
# 	print list_2
# matAdd()

def matAddtwo():
	matrix_1 = [[2, 3], [4, 5]]
	matrix_2 = [[3, 4], [5, 6]]
	rows_1 = [1] * 2
	cols_2 = [1] * 2
	result = [[], []]

	for i in range(len(matrix_1)):
	    for x in range(len(matrix_1[i])):
	        rows_1[i] *= matrix_1[i][x]
	        cols_2[i] *= matrix_2[x][i]

	for i in range(len(matrix_1)):
	    for x in range(len(matrix_1)):
	        result[i].append(rows_1[i] + cols_2[x])

	print matrix_1
	print matrix_2
	print result
matAddtwo()
