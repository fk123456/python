# 元组以小括号的形式展现 ()
# 可以存储任意数据
# 可以根据下标获取数据，但是不支持修改、删除数据

myTuple = (1, 100, "foreign", True)
print(myTuple)

result = myTuple[1]
print(result)

# 定义的元组，里面如果只有一个元素，那么返回该元素的类型
myTuple = (1)
print(myTuple, type(myTuple))

# 判断数据是否在元组里
myTuple = (1, 100, "foreign", True)
result = 1 in myTuple
print(result)
result = 1 not in myTuple
print(result)

# 元组中的下标
result = myTuple.index(100)
print(result)

# 元组中元素的个数
result = myTuple.count("foreign")
print(result)