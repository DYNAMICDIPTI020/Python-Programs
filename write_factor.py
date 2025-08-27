# Program to store, count and find sum of all factors of a given number into factor.txt

factors = []
sum_factors, count = 0, 0

# Open file in write mode
fobj = open("factor.txt", 'w')

no = int(input("Enter any number: "))

for i in range(1, no + 1):
    if no % i == 0:
        sum_factors += i
        count += 1
        factors.append(i)

# Writing to file
fobj.write("All factors = " + str(factors) + "\n")
fobj.write("Number of factors = " + str(count) + "\n")
fobj.write("Sum of factors = " + str(sum_factors) + "\n")

# Close file
fobj.close()
