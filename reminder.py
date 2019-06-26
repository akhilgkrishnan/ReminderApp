import mysql.connector
from mysql.connector import Error
import datetime 
import os
#from server import ReminderCheck

try:
    #Create connection to the mysql database
    mydb = mysql.connector.connect(
        host="localhost",#hostname
        user="reminder",#username
        passwd="akhilgk",#password
        database="sample" #Database name
    )
    mycursor = mydb.cursor()

    #Function for creating reminder
    def reminderCreate():
        print("======Add New Reminder====")
        taskname = input("Enter the Task Name :")
        taskmsg = input("Enter the Task Message :")
        taskdate =input("Enter the Task Date (YY-MM-DD) :")
        tasktime =input("Enter the Task Time (HH:MM:SS) :")
        timedateflag = timedatecheck(taskdate,taskdate)

        if(timedateflag==1):
            print("Date and time already expired")
        else:    


            sql= "INSERT INTO reminders (taskname,taskmsg,taskdate,tasktime) values (%s,%s,%s,%s)"
            val = (taskname,taskmsg,taskdate,tasktime)
            #insert the user entered datas to the database
            mycursor.execute(sql,val)
            mydb.commit()

            os.system('notify-send "You set a reminder "'+taskname) 
            print("New Reminder added Successfully")


    def timedatecheck(remdate,remtime):
        currentDT = datetime.datetime.now() #Read current time and date
        curdate = currentDT.strftime("%Y-%m-%d")
        curtime = currentDT.strftime("%H:%M:%S")
        if(remdate < curdate and remtime < curtime ):
            return 1
    
    def reminderUpdate():
        print("======Reminder Update======")
        
        
        reminderView()
        
        remid = input("Enter the reminder ID you want to Update :")
        sql = "SELECT * FROM reminders WHERE id = %s"
        val =(remid, )
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        if(mycursor.rowcount==1):
            taskname = input("Enter the new  Name :")
            taskmsg = input("Enter the new Reminder Message :")
            taskdate =input("Enter the new Task Date (YY-MM-DD) :")
            tasktime =input("Enter the new Time (HH:MM:SS) :")
            timedateflag = timedatecheck(taskdate,tasktime)
            if(timedateflag==1):
                print("Date and time already expired")
            else:  
                sqlup = "UPDATE reminders SET taskname=%s,taskmsg=%s,taskdate=%s,tasktime=%s WHERE id=%s"
                #UPDATE reminders SET taskname='POda Akhil',taskmsg='Hello',taskdate='19-06-28',tasktime='10:51:10';

                valup = (taskname,taskmsg,taskdate,tasktime,remid)
                mycursor.execute(sqlup,valup)
                mydb.commit()
                sqlupres = "SELECT * FROM reminder where id =%s"
                valupres = (remid, )
                mycursor.execute(sqlupres,valupres)

                update = mycursor.fetchall()
                print("===============================================")
                print("The Reminder id ",remid+" Successfully Updated")
                print("Update Reminder is :")
                for row in update:
                    print("==========================================")
                    print("Reminder ID =",row[0])
                    print("Reminder Created Timestamp = ", row[1], )
                    print("Remainder Name = ", row[2])
                    print("Remainder Message  = ", row[3])
                    print("Remainder Date  = ", row[4])
                    print("Remainder Time  = ", row[5], "\n")
                    print("==========================================`") 
        else:
            print("Please Enter Valid ID")
            reminderUpdate()    
    #Funtion for viewing the reminder
    def reminderView():
        currentDT = datetime.datetime.now() #Read current time and date
        curdate = currentDT.strftime("%Y-%m-%d")
        curtime = currentDT.strftime("%H:%M:%S")
        sql ="SELECT * FROM reminders WHERE taskdate >= %s"
        val = (curdate, )
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        if(mycursor.rowcount<1):
            print("No Reminder Found")
            
        else:
               
            for row in myresult:
                print("==========================================")
                print("Reminder ID =",row[0])
                print("Reminder Created Timestamp = ", row[1], )
                print("Remainder Name = ", row[2])
                print("Remainder Message  = ", row[3])
                print("Remainder Date  = ", row[4])
                print("Remainder Time  = ", row[5], "\n")
                print("==========================================`")    

   
        
          


    print("---Reminder Management System---")
    
       
    while True:
        print("=================================")
        print("Select the Choice")
        print(
            "1:Create Reminder\n"
            "2:Update Reminder\n"
            "3:View Upcomming Reminder\n"
            
            "4:Exit"        
        )
    
        choice = int(input("Enter the Choice :"))
        print("=================================")

        if(choice==1):
            reminderCreate()
            
        elif(choice==2):
            reminderUpdate()
            
        elif(choice==3):
            print("===Reminder Records ===")
            reminderView()
            
        
            
        elif(choice==4):
            break        
        else:
            print("Invalid Choice")

         
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection
    if(mydb.is_connected()):
        mydb.close()
        print("MySQL connection is closed")
