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
    for i in range(30, 45):
        # python
        start = pc()
        fib_pure_py(i)
        end = pc()
        time_python.append(round(end-start, 2))

        # cpp
        start = pc()
        f = Integer(i)
        f.fib()
        end = pc()
        time_cpp.append(round(end-start, 2))

    plt.plot(x=range(30, 45), y=time_python)
    plt.plot(x=range(30, 45), y=time_cpp)
    plt.savefig("fibonacci_timing.png")


    # f = Integer(5)
    # print(f.get())
    # f.set(7)
    # print(f.get())
    # print(f.fib())

if __name__ == '__main__':
    main()