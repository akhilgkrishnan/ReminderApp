import mysql.connector
from mysql.connector import Error
import datetime 
import os


try:
    hostname = "localhost" 
    username = "reminder" #Replace with your username
    password = "akhilgk" #Replace with your password
    database = "sample"#Replace with your database
    mydb = mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        database=database
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema = %s  AND table_name = 'reminders' LIMIT 1",(database, ))
    count = mycursor.fetchall()
    for row in count:
        
        if(row[0]==0):
            mycursor.execute("CREATE TABLE reminders (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,createdtimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, taskname VARCHAR(100),taskmsg VARCHAR(255),taskdate DATE,tasktime TIME)")
            break
    def dayReminder():
        currentDT = datetime.datetime.now()
        curdate = currentDT.strftime("%Y-%m-%d")
        curtime = currentDT.strftime("%H:%M:%S")
        #Give noutification of all reminders on the user login day
        mycursor.execute("SELECT * FROM reminders WHERE taskdate = %s and tasktime > %s",(curdate,curtime ))
        dayevent = mycursor.fetchall()
        if(mycursor.rowcount==0):
            os.system('notify-send "No Reminders Today!"') 
        for row in dayevent:
            os.system('notify-send "Your todays reminder : ' + row[2] + ' at ' + str(row[5]) + '"')


    def ReminderCheck():
        while True:
            currentDT = datetime.datetime.now()
            curdate = currentDT.strftime("%Y-%m-%d")
            curtime = currentDT.strftime("%H:%M:%S")

            

            #Give noutification when the current and date equals to reminder date time
            sql = "SELECT * FROM reminders WHERE taskdate = %s and  tasktime = %s "
            val = (curdate, curtime )
            mycursor.execute(sql,val)
            checkRem = mycursor.fetchall()
            if(mycursor.rowcount==1):
                for row in checkRem:
                    print("You have a reminder "+row[2]+" on "+str(row[4])+" at "+str(row[5]))
                    os.system('notify-send "Your Have a Reminder :"'+row[2])
                    break
            #Removing expired Reminders from the database        
            sql = "DELETE FROM reminders WHERE taskdate<=%s and tasktime<=%s"
            val = (curdate, curtime)
            mycursor.execute(sql,val)
            mydb.commit()
    if __name__ == '__main__': 
        dayReminder()     
        ReminderCheck()   

except Error as e :
    print ("Error while connecting to MySQL", e)


      