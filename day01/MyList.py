# py中列表就是数组，数组就是列表 []
myList = [121, "fangke", 456, "hhh"]
print(myList, type(myList))

# 列表取值
result = myList[0]
print(result)

result = myList[-1]
print(result)

# 增加数据
my_list = []
my_list.append(1)
print(my_list)

my_list.append("中国")
print(my_list)

my_list.append(True)
print(my_list, type(my_list[2]))

my_list.append("True")
print(my_list, type(my_list[3]))

# 指定位置插入数据
my_list.insert(2, "foreign")
print(my_list)

# 插入列表
my_list1 = ["西瓜", "草莓"]
my_list.append(my_list1)
print(my_list)

my_list.extend(my_list1)
print(my_list)

# 修改元素
my_list[0] = "亚洲"
print(my_list)

# 删除元素 五返回值
my_list.remove("中国")
print(my_list)

# 根据下标删除元素
del my_list[0]
print(my_list)

# 使用pop 默认删除最后一个元素，并返回给我们
result = my_list.pop()
print(result)

# 判断指定数据是否在列表中
result = "foreign" in my_list
print(result)

# 根据指定元素查询列表中元素的个数
result = my_list.count(1)
print(result)