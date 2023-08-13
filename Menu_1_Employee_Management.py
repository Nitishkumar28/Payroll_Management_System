import mysql.connector
from tabulate import tabulate

mycon = mysql.connector.connect(host="localhost", user="root", password="nps123", database="project")
cursor = mycon.cursor()
cursor.execute("drop table if exists EMPLOYEE")
cursor.execute("drop table if exists Department")
cursor.execute("create table Employee(Employee_ID int primary key not null,Employee_Name varchar(20),Date_of_join date not null,Gender char(1),Phone_number bigint not null, Aadhar_card_no char(20) not null,Email_ID varchar(30),Address text not null)")
cursor.execute("insert into Employee values(1,'Ramesh','2020/02/12','M',9860521453,'1234 4367 7890 5621','ramesh02@gmail.com','flat no 999 opendoor apartments,Bangalore')")
cursor.execute("insert into Employee values(2,'Cody','2018/03/13','M',9678902345,'7890 2376 4907 1790','codyx13@gmail.com','flat no 890 heavensgate apartments,Bangalore')")
cursor.execute("insert into Employee values(3,'Shiv','2017/10/01','M',8889576565,'6809 5780 1090 6666','shiviv70@gmail.com','flat no 303 urban apartments,Bangalore')")
cursor.execute("insert into Employee values(4,'Amy','2019/09/10','F',9900521453,'5680 9800 4589 2222','amyQ2@gmail.com','flat no 111 bluesky apartments,Bangalore')")
cursor.execute("insert into Employee values(5,'Akhila','2018/04/27','F',9645789033,'9090 6070 4566 1234','akhila70@gmail.com','flat no 903 bluesky apartments,Bangalore')")
cursor.execute("insert into Employee values(6,'Zoya','2019/03/30','F',7908974560,'9234 8378 9060 7777','ZoyaZ78@gmail.com','flat no 45 breezeway apartments,Bangalore')")
cursor.execute("insert into Employee values(7,'Akhil','2017/05/15','M',7908974590,'7890 8378 2468 7777','akhileats9@gmail.com','flat no 30 breezeway apartments,Bangalore')")
cursor.execute("insert into Employee values(8,'Nadia','2017/03/09','F',7090012345,'7640 5031 2021 2177','nads03@gmail.com','flat no 690 oceanshore apartments,Bangalore')")
cursor.execute("insert into Employee values(9,'Alvin','2020/12/01','M',8577633464,'2094 7051 9554 8967','Alvinchip4@gmail.com','flat no 01 breezeway apartments,Bangalore')")
cursor.execute("insert into Employee values(10,'Andy','2019/11/08','M',9976391290,'3190 6060 8809 5678','AndyL90@gmail.com','flat no 001 millenial apartments,Bangalore')")



def add():
    while True:
        print("Enter Employee details:\n")
        emp_id = int(input("Enter Employee ID: "))
        emp_name = input("Enter Employee Name: ")
        doj = input("Enter Date of Join(YYYY/MM/DD): ")
        gen = input("Enter Gender(M/F): ")
        phno = int(input("Enter Phone Number: "))
        adhr = input("Enter Aadhar card no:")
        email = input("Enter Email ID: ")
        addres = input("Enter Employee Address: ")
        cursor.execute("INSERT INTO EMPLOYEE VALUES({},'{}','{}','{}',{},'{}','{}','{}') ".format(emp_id, emp_name, doj, gen, phno,adhr, email, addres))
        mycon.commit()
        cursor.execute("select * from employee where Employee_ID={}".format(emp_id,))
        x=cursor.fetchall()
        print("\nThe record that will be inserted is:")
        l = ["Employee ID", "Employee_name", "Date_of_join", "Gender", "Phone_number", "Aadhar_card_no", "Email_Id","Address"]
        print(tabulate(x, headers=l,tablefmt='fancy_grid'))
        ch = input("\nWould you like to continue(y/n): ")
        print()
        if ch == "n":
            break


def delete():
    id = int(input("Enter Employee ID to delete record: "))
    cursor.execute("select * from employee where Employee_ID={}".format(id,))
    p=cursor.fetchall()
    print("\nThe deleted record is:")
    l=["Employee ID","Employee_name","Date_of_join","Gender","Phone_number","Aadhar_card_no","Email_Id","Address"]
    print(tabulate(p, headers=l, tablefmt='fancy_grid'))
    cursor.execute("DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID={}".format(id,))
    mycon.commit()


while True:
    print("1. Add Record(s) \n2. Delete Record \n3. Return to main menu\n")
    n = int(input("Enter your choice: "))
    if n == 1:
        add()
        print("Record(s) added successfully\n")
    elif n == 2:
        delete()
        print("\nRecord deleted successfully\n")
    elif n == 3:
        break
    else:
        print("Wrong option")

mycon.close()
