from math import factorial

def fact(n):
	if n==1:
		return 1
	else:
	    return n*factorial(n-1)	


n=int(input("Enter the nunber"))
print("Factorial of " ,n, "is", fact(n))
