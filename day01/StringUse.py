# 可以使用"" / '' / """""" 三种引号形式封装字符串数据
str = "苹果橘子香蕉"
# str = '苹果橘子香蕉'
# str = """苹果橘子香蕉"""
print(str)
# 字符串查找, 返回数据对应的元素位置, find如果找不到元素则返回-1 index则报错
strValue = '123'
result = strValue.find("1")
print(result)

result = strValue.index("1")
print(result)

# 替换字符串
result = str.replace("苹果", "apple")
print(result)

# 分隔字符串 如果没有逗号，则返回字符串整体的列表。如果有逗号，则按逗号进行分隔
result = str.split(",")
print(result)
str = "苹果,橘子,香蕉"
result = str.split(",")
print(result)

# 把字符串按指定字符分隔
str = "aaabbccc"
result = str.partition("bb")
print(result)

strFlag = "-"
result = strFlag.join(str)
print(result)

# 分隔列表
myList = ["1", "2", "3"]
result = strFlag.join(myList)
print(result)


# 判断字符串是否以指定数据开头 返回 True或False
str = "http://www.baidu.com"
result = str.startswith("http")
print(result)

# 判断字符串是否以指定数据结尾 返回 True或False
result = str.endswith("xxx")
print(result)

# 去除空格 全部 左边 右边
str = " hello "
result = str.strip()
print(result)
result = str.lstrip()
print(result)
result = str.rstrip()
print(result)

# 去除指定数据 (如果不传数据，默认去除空格，左右两边）
str = "awaewy"
result = str.strip("a")
print(result)
