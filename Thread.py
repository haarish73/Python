import threading
import time

# def cal_fun(n):
#     print("thread", n)
#
# t1 = threading.Thread(target=cal_fun, args=(10,))
# t1.start()
#
# square
#
#
# def f_squar(n):
#     print("square=",n*n)
# t1 = threading.Thread(target=f_squar,args=(5,))
# t1.start()


# cube


def f_cube(n):
    print("cube=",n*n*n)
t1 = threading.Thread(target=f_cube,args=(5,))
t1.start()
time.sleep(10)