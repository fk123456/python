# 修改全局变量的值
score = 100

def myFunc():
    global score
    score = 99
    print(score)
    return score

result = myFunc()
print(result)