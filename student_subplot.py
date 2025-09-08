import csv
import matplotlib.pyplot as plt
CampName , gender , cast = [], [] ,[]
obj = open("student.csv", "r")
records = csv.reader(obj)
next (records)
for record in records :
	gender .append (record [2])
	cast .append(record [3])
	CampName .append(record[4])
#plot1
#print (gender)
plt . subplot (2,2,1)
color = ["green", "red"]
plt.pie([gender.count('male'),gender.count('female')],labels=["Male", "Female"],colors=color,autopct="%.2f%%")
plt . title("Male vs Female")
plt .legend(['Male' ,'Female'])



#plot 2
plt.subplot (2,2,2)
plt.bar(["Microsoft","WIPRO","NOT","TCS","Microsoft","CISCO" ,"NOT" ,"TCS","WIPRO" ,"DEL"],[CampName.count("Microsoft"),CompanyName.count("WIPRO"),CompanyName.count("NOT"),CompanyName.count("TCS"),CompanyName.count("Microsoft"),CompanyName.count("CISCO"),CompanyName.count("NOT"),CompanyName.count("TCS"),Companyname.count("WIPRO"),CompanyName.count("DEL")],color=["red","green","blue","black"])
plt.title("Placement Status")
plt.xlabel("CompanyName")
plt.ylabel("Number of students placed differt company")
plt.grid(axis='y')



#plot 3
#plot 3
plt.subplot (2,2,4)
plt.pie([Cast.count('GEN'),Cast.count('GEN'),Cast.count('SC'),Cast.count('ST'),Cast.count('GEN'),Cast.count('OBC'),Cast.count('SC') ,Cast.count('GEN'),Cast.count('SC'),Cast.count('ST')])
plt.title("Cast Report")
plt.legend(["GEN", "SC", "ST" ,"OBC" ])


plt.show()




