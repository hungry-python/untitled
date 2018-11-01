import time
def time_counting(fun):
    def inner(*args,**kwargs):
        time1=time.time()
        fun(*args,**kwargs)
        time2=time.time()
        time_count=time2-time1
        print("所用的时间为：",time_count)
    return inner
@time_counting
def f(x):
    s = 0
    for i in range(1, x + 1):
        s += i
    print("该函数计算结果为：",s)

if __name__ == '__main__':
    f(10000)

