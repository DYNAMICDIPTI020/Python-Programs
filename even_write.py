'''write a  program to print all the even.txt and all odd number in odd.txt and
find the sum of all the even number and odd number in rang eof 1 to 500'''
fobj1 = open  ("even.txt" , 'w')
fobj2 = open ("odd.txt" , 'w')

evensum , oddsum = 0 ,0
for i in range (1 , 500+1) :
    if i % 2 == 0 :
        fobj1 .write (str(i) + "\t")
        evensum += i
    else  :
        fobj2 .write (str(i) + "\t")
        oddsum += i
fobj1 . write ("\n sum of all even number = "+ str(evensum))
fobj2 . write ("\n sum of all odd number = "+ str (oddsum))

fobj1.close ()
fobj2.close()

