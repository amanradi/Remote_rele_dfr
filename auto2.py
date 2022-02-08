import mysql.connector


#----------------------------------hubung database------------------------------
mydb = mysql.connector.connect(
  host="10.94.79.29",
  port="3306",
  user="rachman",
  password="rachman12345",
  database="status_cb"
)

#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("DESCRIBE data_status_cb ;")
myresult = mycursor.fetchall()
 
for x in myresult:
    print(x)




#-----------------------------------cek status CB tiap invertal tertentu---------------------------

def checking():
    while 