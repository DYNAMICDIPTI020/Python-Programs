''' this is  user define module this module is used to check how to access
all the attribute present in this module'''

LIT = 3.14

#max function take two argument same as n1 and n2 and return max element 
def Max(no1 , no2) :
        return n1 if n1 > n2 else n2 , "is max"

#check function take one argument same as no and check return that
#number is +ve or -ve
def Check (no):
    if no  > 0 :
        return "+ve"
    else :
        return "-ve"

#name funtion find area of circle where r value is given
def Area (r):
    return 3.14 * r ** 2
#this add function make addition of two number
def Add (n1 , n2 ):
    print("sum =", n1 + n2)

