n=int(input("enter a number whose factorial u want to compute"))
##factorial 
fact=1
if n<0:
	print("the factorial does not exist")
elif n==0:
	print("factorial=1")
else:
	for i in range(1,n+1):
		fact=fact*i
	print(f"the factorial is {fact}")
