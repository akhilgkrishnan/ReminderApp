# ReminderApp
This is simple Database application for Creating , Updating and Viewing reminders. And also you get  notification in the Desktop when a reminder event occur.

This app is worked fully based on the command line and it is build in python.


 It works in both Python2.7 or Python3

## How to Run

-: Install libraries : `$ pip install -r requirement.txt`   
-: Change host,user,password according to your mysql server in server.py and reminder.py

    mydb = mysql.connector.connect(
        host="localhost", 
        user="reminder", //Replace reminder with your name
        passwd="akhilgk", //Replace akhilgk with your own password
        database="sample" //Add your database name
    )
3=: Open the terminal    
4: run  ` $ python server.py`       
5: without closing the current terminal open a new terminal and run `$python reminder.py`  then you get a choice option like below,

Reminder Management System
=================================
Select the Choice   
1:Create Reminder  
2:Update Reminder    
3:View Upcomming Reminder    
4:Exit    
Enter the Choice :

6: Select appropreate option    
7: Done




