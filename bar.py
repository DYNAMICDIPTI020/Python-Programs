import matplotlib.pyplot as plt
subname = ['Math','Odia', 'phy', 'Che', 'it' ,'Eng']
colors = ['red' , 'blue','yellow', 'orange', 'black', 'pink']
mark = [ 78 , 90 , 83 , 89 , 97 ,88]

#plt .bar (subname , mark , color = colors , width = 0.4)
plt .title ("secure mark in each subject")
plt .xlabel("Subject name ")
plt .ylabel("Mark secure by each subject out of 100")
plt.grid (axis = 'y' , color = 'blue' , linewidth = 1 , linestyle = '-.')



plt .barh(subname , mark , color = colors , height = 0.3)
plt .title ("secure mark in each subject")
plt .ylabel("Subject name ")
plt .xlabel("Mark secure by each subject out of 100")
plt.grid (axis = 'x' , color = 'blue' , linewidth = 1 , linestyle = '-.')
plt .show()