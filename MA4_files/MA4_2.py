#!/usr/bin/env python3

from integer import Integer

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fib())

if __name__ == '__main__':
	main()