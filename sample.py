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
            print(curdate)
            print(curtime)
        
            mycursor.execute("SELECT taskname FROM reminder WHERE taskdate 'curdate'")
            checkRem = mycursor.fetchall()
            print(checkRem)
            if(mycursor.rowcount>=1):
                for row in checkRem:
                
                    os.system('notify-send "You have a reminder"'+row[0])
       

         
except Error as e :
    print ("Error while connecting to MySQL", e)

      