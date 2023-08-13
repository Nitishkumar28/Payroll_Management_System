import mysql.connector
from tabulate import tabulate

mycon = mysql.connector.connect(host="localhost", user="root", password="nps123", database="project")
cursor = mycon.cursor()
cursor.execute("drop table if exists EMPLOYEE")
cursor.execute("drop table if exists Department")
cursor.execute("create table Employee(Employee_ID int primary key not null,Employee_Name varchar(20),Date_of_join date not null,Gender char(1),Phone_number bigint not null, Aadhar_card_no char(20) not null,Email_ID varchar(30),Address text not null)")
cursor.execute("create table Department(Employee_ID int primary key not null,Department_name varchar(40) not null,Designation varchar(30),No_of_projects int not null)")
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
cursor.execute("insert into Department values(1,'Production','Employee',0)")
cursor.execute("insert into Department values(2,'Research and Development','Cheif developing officer',2)")
cursor.execute("insert into Department values(3,'Purchasing','Cheif purchasing officer',3)")
cursor.execute("insert into Department values(4,'Production','Cheif producting officer',1)")
cursor.execute("insert into Department values(5,'Marketing','Cheif marketing officer',2)")
cursor.execute("insert into Department values(6,'Production','Employee',1)")
cursor.execute("insert into Department values(7,'HR','Cheif HR officer',3)")
cursor.execute("insert into Department values(8,'Accounting and Finance','Cheif officer',4)")
cursor.execute("insert into Department values(9,'Graphics and animation','Employee',0)")
cursor.execute("insert into Department values(10,'Animation','Employee',1)")

def desig():
    des=input("Enter Designation: ")
    cursor.execute("SELECT Employee.Employee_ID, Employee_name, Designation FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID and Designation='{}' ".format(des,))
    x=cursor.fetchall()
    l=["Employee_ID","Employee_name","Designation",]
    print(tabulate(x,headers=l,tablefmt='fancy_grid'))
    mycon.commit()

def dept():
    dep=input("Enter Department: ")
    cursor.execute("SELECT Employee.Employee_ID, Employee_name, Department_name FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID and Department_name='{}'".format(dep))
    x=cursor.fetchall()
    l=["Employee_ID","Employee_name","Department_name",]
    print(tabulate(x,headers=l,tablefmt='fancy_grid'))
    mycon.commit()

def salary():
    print("Order salary from:\n1. Low to High\n2. High to Low\n")
    ch=int(input("Enter your choice: "))
    if ch==1:
        cursor.execute("SELECT Employee.Employee_ID, Employee_name, Salary FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=Emp_Salary.Employee_ID ORDER BY salary")
    else:
        cursor.execute("SELECT Employee.Employee_ID, Employee_name, Salary FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=Emp_Salary.Employee_ID ORDER BY salary desc")
    x=cursor.fetchall()
    l=["Employee_ID","Employee_name","Salary",]
    print(tabulate(x,headers=l,tablefmt='fancy_grid'))
    mycon.commit()

def proj():
        print("Order Projects from:\n1. Low to High\n2. High to Low\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            cursor.execute(
                "SELECT Employee.Employee_ID, Employee_name, No_of_projects FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID ORDER BY No_of_projects")
        else:
            cursor.execute(
                "SELECT Employee.Employee_ID, Employee_name, No_of_projects FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID ORDER BY No_of_projects desc")
        x = cursor.fetchall()
        l = ["Employee_ID", "Employee_name", "No_of_projects", ]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
        mycon.commit()

while True:
    print("View Employee Details based on given criteria:\n1.Designation\n2.Department\n3.Salary\n4.No of projects\n5.Return to Main Menu\n")
    n=int(input("Enter your choice: "))
    if n==1:
        print("\nEmployee Details Based On Designation:\n")
        desig()
        print()
    elif n==2:
        print("\nEmployee Details Based On Department:\n")
        dept()
        print()
    elif n==3:
        print("\nEmployee Details Based On Salary:\n")
        salary()
        print()
    elif n==4:
        print("\nEmployee Details Based On No of projects")
        proj()
        print()
    elif n==5:
        break
    else:
        print("Wrong option")

mycon.close()

