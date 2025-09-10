from pymysql import * 
conobj = connect (host = "localhost" , user = 'root', password='', port=3306)
print(conobj)
curobj = conobj .cursor ()



curobj. close()
conobj . close()