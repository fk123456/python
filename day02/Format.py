# 格式化输出符
# %s 格式化输出字符串
# %d 格式化输出整形
# %f 格式化输出浮点类型
# %x 格式化输出十六进制
str = "foreign"
print("my name is %s" %str)

score = 100
print("my score is %d" %score)

# 默认保留六位小数，四舍五入
score = 100.511
print("my score is %f" %score)
print("my score is %.2f" %score)

score = 11
print("my score is %x" %score)