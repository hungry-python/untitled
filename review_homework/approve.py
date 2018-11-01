dic={"张三":"123","李四":"1234","王五":"12345"}
def approving(fun):
    def inner(*args,**kwargs):
        name=input("请输入用户名：")
        passwd=input("请输入密码：")
        if name in dic.keys():
            if passwd==dic[name]:
                fun(*args,**kwargs)
            else:
                print("密码输入错误！")
        else:
            print("该用户名不存在...")
    return inner

@approving
def f(x):
    s = 0
    for i in range(1, x + 1):
        s += i
    print("该函数计算结果为：", s)

if __name__ == '__main__':
    f(100)


