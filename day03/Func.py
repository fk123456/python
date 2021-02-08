# 函数
# 定义
def myFunc():
    print("hahaha")

# 调用
myFunc()

# 带参数
def funcArg(name, age):
    print("我的名字是 %s, 我的年龄是%d" %(name, age))

funcArg("foreign", 18)

# 使用关键字传参
funcArg(age=18, name="foreign")

# 带返回值
def funcReturn():
    return 10

result = funcReturn()
print(result)