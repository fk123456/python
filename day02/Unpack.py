# 拆包 把数据都遍历出来
# 字符串
str = "123"
a, b, c = str
print(a, b, c)

# 列表
myList = [1,2]
num1, num2 = myList
print(num1, num2)

# 元组
myTuple = (1, 5)
num1, num2 = myTuple
print(num1, num2)

# 字典
myDict = {"name": "foreign", "age": 18}
a, b = myDict
print(a, b)

myDict = {"name": "foreign", "age": 18}.values()
a, b = myDict
print(a, b)

# 集合
mySet = {1, 2}
a, b = mySet
print(a, b)