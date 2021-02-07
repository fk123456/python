# 字典，大括号的展现形式，{key:value}
# 可变类型：变量，列表 不可变类型：元组，数字
myDict = {"name": "foreign", "age": 18}
print(myDict, type(myDict))

# 取值
result = myDict["name"]
print(result)

# 如果取值为空的话，会报错，可以采用get方法, 返回为None
result = myDict.get("sex")
print(result)

# 如果该key不存在，则get方法也可以作为赋值操作
result = myDict.get("sex", "男")
print(result)

# 新增
myDict["color"] = "red"
print(myDict)

# 修改
myDict["color"] = "black"
print(myDict)

# 删除 会删除整个myDict name 报错'myDict' is not defined
# del myDict
del myDict["color"]
print(myDict)

# 随机删除
myDict["color"] = "white"
myDict["number"] = 15990157013
print(myDict)
myDict.popitem()
print(myDict)

# 指定元素删除
result = myDict.pop("age")
print(myDict, result)

# 遍历所有的values
result = myDict.values()
print(result)

# 遍历所有的keys
result = myDict.keys()
print(result)

# 判断key是否在字典中
result = "name" in myDict
print(result)

# 遍历keys和values
for keys, values in myDict.items():
    print(keys, values)