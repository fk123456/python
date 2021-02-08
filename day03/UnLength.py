# 不定长参数
def myFunc(*args):
    print(args, type(args))
    result = 0
    for value in args:
        result += value
    return result

result = myFunc(1, 2, 3, 4)
print(result)

# 不定长位置参数
def myFunc1(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

myFunc1(a=1, b=2)

# 缺省函数
def myFunc2(num1, num2=2):
    return num1 + num2

result = myFunc2(1)
print(result)

def myFunc3(*args):
    print(args, *args, type(args))

myFunc3(1, 2, 3)

# 嵌套函数
def myFunc4():
    print("hhh")
    def myFunc5():
        print("aaa")
    myFunc5()

myFunc4()

def myFunc6():
    print("aaaaa")
    def myFunc7():
        print("bbbbb")
    # 返回函数名称
    return myFunc7

result = myFunc6()
# 调用内部函数
result()
