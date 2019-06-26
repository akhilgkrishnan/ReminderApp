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
    #mycursor.execute("CREATE TABLE reminders (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,createdtimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, taskname VARCHAR(100),taskmsg VARCHAR(255),taskdate DATE,tasktime TIME)")


   
        
          

    def ReminderCheck():
        while True:
            currentDT = datetime.datetime.now()
            curdate = currentDT.strftime("%Y-%m-%d")
            curtime = currentDT.strftime("%H:%M:%S")
            
            sql = "SELECT * FROM reminders WHERE taskdate = %s and  tasktime = %s"
            val = (curdate, curtime )
            mycursor.execute(sql,val)
            checkRem = mycursor.fetchall()
            
            if(mycursor.rowcount==1):
                for row in checkRem:
                    print("You have a reminder "+row[2]+" on "+str(row[4])+" at "+str(row[5]))
                    print(row)
                    os.system('notify-send "Your Have a Reminder :"'+row[2])
                    break
            sql = "DELETE FROM reminders WHERE taskdate=%s and tasktime=%s"
            val = (curdate, curtime)
            mycursor.execute(sql,val)
            mydb.commit()

    ReminderCheck()   
            
except Error as e :
    print ("Error while connecting to MySQL", e)


      