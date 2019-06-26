import mysql.connector
from mysql.connector import Error
import datetime 
import os


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="reminder",
        passwd="akhilgk",
        database="sample"
    )
    mycursor = mydb.cursor()
    #mycursor.execute("CREATE TABLE reminder (createdtimestamp TIMESTAMP, taskname VARCHAR(100),taskmsg VARCHAR(255),taskdate DATE,tasktime TIME)")

   
        
          

    def ReminderCheck():
        while True:
            currentDT = datetime.datetime.now()
            curdate = currentDT.strftime("%Y-%m-%d")
            curtime = currentDT.strftime("%H:%M:%S")
            
            sql = "SELECT * FROM reminder WHERE taskdate = %s and  tasktime = %s"
            val = (curdate, curtime)
            mycursor.execute(sql,val)
            checkRem = mycursor.fetchall()
            
            if(mycursor.rowcount==1):
                for row in checkRem:
                    print("You have a reminder "+row[1]+" on "+str(row[3])+" at "+str(row[4]))
                    
                    os.system('notify-send "Your Have a Reminder :"'+row[1])
                    break
                sql = "DELETE  FROM reminder WHERE taskdate = %s and  tasktime = %s"
                val = (curdate, curtime)
                mycursor.execute(sql,val)
                mydb.commit()
       
            
except Error as e :
    print ("Error while connecting to MySQL", e)

      