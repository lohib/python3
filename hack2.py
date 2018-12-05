## program to test the if else statements
N=int(input("ENter the number:"))
if N%2==1:
	print("Weird")
elif N%2==0 and 2<=N<=5:
	print("Not Weird")
elif N%2==0 and 6<=N<=20:
	print("Weird")
else:
	print("Not Weird")

