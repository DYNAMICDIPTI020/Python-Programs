#write a program to find max between two number 
def Max (no1 , no2 ) :
	print(no1 if no1 > no2 else no2 ,"max")
no1 = int(input("Enter the first number"))
no2 = int(input("Enter the second number"))
Max (no1, no2)
