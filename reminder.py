import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="reminder",
  passwd="akhilgk",
  database="sample"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

def reminderCreate():
    print("Enter the Date (DD/MM/YYY) :")
    
def reminderUpdate():
def reminderView():        

print("---Reminder Management System---")
while True:
    print("=================================")
    print("Select the Choice")
    print(
        "1:Create Reminder\n"
        "2:Update Reminder\n"
        "3:View Reminder\n"
        "4:Exit"        
    )
    
    choice = int(input("Enter the Choice :"))
    print("=================================")

    if(choice==1):
        reminderCreate()
        print("Create")
    elif(choice==2):
        def reminderUpdate():
        print("Update")
    elif(choice==3):
        def reminderView(): 
        print("View")
    elif(choice==4):
        break        
    else:
        print("Invalid Choice")

