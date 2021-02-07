# while循环
num = 0
while num < 5:
    print(num)
    num += 1

print("-----------")

# 默认起始数据为0，终止数据为5，默认步长为1
for value in range(5):
    print(value)

print("-----------")

# Enumerate 可以直接遍历出下标
num = [1, 2, 3, "apple", 99]
result = enumerate(num)
print(type(result))
for item, value in result:
    print(item , value)
print("-----------")

# 默认起始数据为0，终止数据为5，步长为3
for value in range(0, 6, 3):
    print(value)

print("-----------")

# while、for循环和else结合使用
num = 3
while num >= 1:
    print(num)
    num -= 1
else:
    print("打印完成")

print("-----------")

for value in range(3):
    print(value)
else:
    print("打印完成")

print("-----------")

# continue和break 必须结合循环使用
num = 3
while num > 0:
    num -= 1
    if num == 2:
        continue
    print(num)
else:
    print("循环结束")

print("-----------")

for value in range(3):
    print(value)
    value += 1
    if value == 2:
        break
else:
    print("循环结束")