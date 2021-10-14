#!/usr/bin/env python3
from time import perf_counter as pc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from integer import Integer

def fib_pure_py(n):
    if n <= 1:
        return n
    else:
        return(fib_pure_py(n-1) + fib_pure_py(n-2))


def main():
    time_python = []
    time_cpp = []
    for i in range(10, 15):
        # python
        start = pc()
        fib_pure_py(10)
        end = pc()
        print(round(end-start, 2))
        time_python.append(round(end-start, 2))

        # cpp
        start = pc()
        f = Integer(i)
        f.fib()
        end = pc()
        print(round(end-start, 2))
        time_cpp.append(round(end-start, 2))

    print(time_python)
    print(time_cpp)
    plt.plot(list(range(10, 15)), time_python)
    plt.plot(list(range(10, 15)), time_cpp)
    # plt.savefig("fibonacci_timing.png")


    # f = Integer(5)
    # print(f.get())
    # f.set(7)
    # print(f.get())
    # print(f.fib())

if __name__ == '__main__':
    main()