# ReminderApp
This is simple Database application for Creating , Updating and Viewing reminders. And also you get  notification in the Desktop when a reminder event occur.

This app is worked fully based on the command line and it is build in python.

## Prerequisites

- Python 3.4 or greater
- pip
- Virtualenv
- MySql

## Installing
```
$ python3 -m venv reminder && cd reminder
$ git clone https://github.com/AkhilGKrishnan/ReminderApp.git 
$ source bin/activate
$ cd ReminderApp
$ pip install -r requirement.txt

```
 

## How to Run

  
- Change host,user,password according to your mysql server in server.py and reminder.py
```
mydb = mysql.connector.connect(
    host="localhost", 
    user="reminder", //Replace reminder with your name
    passwd="akhilgk", //Replace akhilgk with your ownpassword
    database="sample" //Add your database name
)
```  
- Open the terminal    
- run  ` $ python server.py`       
- without closing the current terminal open a new terminal and run `$python reminder.py`  then you get a choice option like below,

### Reminder Management System-

Select the Choice   
1:Create Reminder  
2:Update Reminder    
3:View Upcomming Reminder    
4:Exit    
Enter the Choice :

- Select appropreate option    
- Done




