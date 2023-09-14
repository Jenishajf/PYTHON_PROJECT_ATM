import datetime
import smtplib
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="account_db"
)
#*********************************
mycursor=mydb.cursor()
#*********************************
#insert data into db
def insert_data():
    sql="insert into transfer_details (Account_Holder,Bank_Name,Branch_Name,Account_No,IFSC_Code,Email_id,Phone_No,Total_Amount,Beneficiary_Name,Beneficiary_Bank_Name,Beneficiary_Branch_Name,Beneficiary_IFSC_Code,Beneficiary_Account_No,Beneficiary_Phone_No,Beneficiary_Email_id,Transfer_Amount,Pin_No,Date,Time,Day,Month,Balance_Amount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print("*********Insert Data*********")
    Account_Holder=input("Enter your Full Name:")
    Bank_Name=input("Enter your Bank Name:")
    Branch_Name=input("Enter your Bank Branch Name:")
    Account_No=int(input("Enter your Account Number:"))
    IFSC_Code=input("Enter your Bank IFSC code:")
    Email_id=input("Enter your Email Id:")
    Phone_No=int(input("Enter your phone number:"))
    Total_Amount=100000
    print(f"Total Amount={Total_Amount}")
    Beneficiary_Name=input("Enter Beneficiary Name:")
    Beneficiary_Bank_Name=input("Enter Beneficiary Bank Name:")
    Beneficiary_Branch_Name=input("Enter Beneficiary Bank Branch Name:")
    Beneficiary_Account_No=int(input("Enter Beneficiary Account Number:"))
    Beneficiary_IFSC_Code=input("Enter Beneficiary Bank IFSC code:")
    Beneficiary_Phone_No=int(input("Enter Beneficiary phone number:"))
    Beneficiary_Email_id=input("Enter Beneficiary Email Id:")
    Transfer_Amount=int(input("Enter the amount you want to transfer:"))
    Pin_No=int(input("Enter your UPI Pin No:"))
    x=datetime.datetime.now()
    Date=x.strftime("%d/%b/%Y")
    print(f"Date={Date}")
    Time=x.strftime("%H:%M:%S")
    print(f"Time={Time}")
    Day=x.strftime("%A")
    print(f"Day={Day}")
    Month=x.strftime("%B")
    print(f"Month={Month}")
    Balance_Amount=Total_Amount-Transfer_Amount
    print(f"Balance_Amount={Balance_Amount}")
    val=(Account_Holder,Bank_Name,Branch_Name,Account_No,IFSC_Code,Email_id,Phone_No,Total_Amount,Beneficiary_Name,Beneficiary_Bank_Name,Beneficiary_Branch_Name,Beneficiary_IFSC_Code,Beneficiary_Account_No,Beneficiary_Phone_No,Beneficiary_Email_id,Transfer_Amount,Pin_No,Date,Time,Day,Month,Balance_Amount)
    mycursor.execute(sql,val)
    mydb.commit()# save data into db
    print("*****Your Amount Transfered Successfully...*****")
    try:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("jenishasundari@gmail.com", "lgjknelwwwyimnoo")
        message=(f"Dear User,A/C Debited by {Transfer_Amount} on {Date} trf to {Beneficiary_Name} and Balance Amount {Balance_Amount}-{Bank_Name}")
        s.sendmail("jenishasundari@gmail.com",Email_id,message)
        s.quit()
        print("Mail send successfully to Account Holder......")
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("jenishasundari@gmail.com", "lgjknelwwwyimnoo")
        message=(f"Dear Customer,Your A/C {Beneficiary_Account_No} is credited by Rs {Transfer_Amount} on {Date} by {Account_Holder}-{Bank_Name}")
        s.sendmail("jenishasundari@gmail.com",Beneficiary_Email_id,message)
        s.quit()
        print("Mail send successfully to Beneficiary......")
    except:
        print("sorry mail not send")
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_function()
    else:
        print("***THANKS FOR VISITING......***")
#view data into db
def view_data():
    mycursor.execute("select * from transfer_details")
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_function()
    else:
        print("***THANKS FOR VISITING......***")
#update data into db
def update_data():
    change=input("What you want change type like this ie. column name='update name':")
    fullname=input("Enter your Full name in single quotes:")
    sql=(f"update transfer_details set {change} where Account_Holder={fullname}")   
    mycursor.execute(sql)
    mydb.commit()
    print("Updated successfully....")
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_function()
    else:
        print("***THANKS FOR VISITING......***")
#delete data into db
def delete_data():
    column_name=input("which column you want to delete:")
    delete_data=input(f"which data you want to delete in {column_name} column:")
    sql=(f"delete from transfer_details where {column_name}={delete_data}")
    mycursor.execute(sql)
    mydb.commit()
    print("Deleted successfully.....")
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_function()
    else:
        print("***THANKS FOR VISITING......***")
def main_function():
    try:
        print("******CRUD******")
        print("1--->insert data")
        print("2--->view data")
        print("3--->update data")
        print("4--->delete data")
        user=int(input("Enter a number:"))
        if user==1:
            insert_data()
        elif user==2:
            view_data()
        elif user==3:
            update_data()
        elif user==4:
            delete_data()
        else:
            print("***Pls check your number...***")
    except:
        print("pls type number only")
main_function()