'''wap to write all the number in a range & find sum of all number in to a file name number.txt'''
fobj = open("number.txt", "w")

res = 0
for i in range(1 , 100+1) :
    fobj . write (str (i) + "\t")
    res = res + i 


fobj =("\n sum of all the number is  "+ str(res))
fobj.close ()
