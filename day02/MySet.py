# 集合：以大括号的形式展现 不能有重复的数据

# 不可以采用 空{}进行展现
mySet = {}
print(mySet, type(mySet))

# 定义一个空的集合
mySet = set()
print(mySet, type(mySet))

mySet = {1, 2, "hhh", 4}
print(mySet)

# 新增数据
mySet.add("foreign")
print(mySet)

# 删除数据 (不能删除不存在的数据）
mySet.remove(2)
print(mySet)

# 此方法删除不存在的数据，不会报错
mySet.discard(5)
print(mySet)

# 循环
for value in mySet:
    print(value)

# 将XX转换为列表
result = list(mySet)
print(result)

# 将XX转换为元组
result = tuple(result)
print(result)

# 将XX转换为集合
result = set(result)
print(result)

