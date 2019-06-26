import mysql.connector
from mysql.connector import Error
import datetime 
import os
from sample import ReminderCheck

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="reminder",
        passwd="akhilgk",
        database="sample"
    )
    mycursor = mydb.cursor()
    #mycursor.execute("CREATE TABLE reminder (createdtimestamp TIMESTAMP, taskname VARCHAR(100),taskmsg VARCHAR(255),taskdate DATE,tasktime TIME)")

    def reminderCreate():
        print("======Add New Reminder====")
        taskname = input("Enter the Task Name :")
        taskmsg = input("Enter the Task Message :")
        taskdate =input("Enter the Task Date (YY-MM-DD) :")
        tasktime =input("Enter the Time Time (HH:MM:SS) :")
        sql= "INSERT INTO reminder (taskname,taskmsg,taskdate,tasktime) values (%s,%s,%s,%s)"
        val = (taskname,taskmsg,taskdate,tasktime)
        mycursor.execute(sql,val)
        mydb.commit()
        os.system('notify-send "You have a reminder"'+taskname) 


  
    
    #def reminderUpdate():
    def reminderView():
        mycursor.execute("SELECT * FROM reminder")
        myresult = mycursor.fetchall()
        for row in myresult:
            print("==========================================")
            print("Reminder Created Timestamp = ", row[0], )
            print("Remainder Name = ", row[1])
            print("Remainder Message  = ", row[2])
            print("Remainder Date  = ", row[3])
            print("Remainder Time  = ", row[4], "\n")
            print("==========================================")    

   
        
          


    print("---Reminder Management System---")
    
       
    while True:
        print("=================================")
        print("Select the Choice")
        print(
            "1:Create Reminder\n"
            "2:Update Reminder\n"
            "3:View Upcomming Reminder\n"
            "4:Live\n"
            "5:Exit"        
        )
    
        choice = int(input("Enter the Choice :"))
        print("=================================")

        if(choice==1):
            reminderCreate()
            print("New Reminder added Successfully")
        elif(choice==2):
            #reminderUpdate():
            print("Update")
        elif(choice==3):
            reminderView()
            print("View")
        elif(choice==4):
            ReminderCheck()
        elif(choice==5):
            break        
        else:
            print("Invalid Choice")

         
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mydb.is_connected()):
        mydb.close()
        print("MySQL connection is closed")
