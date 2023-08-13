import mysql.connector
from tabulate import tabulate

mycon=mysql.connector.connect(host="localhost",user="root",password="nps123",database="project")
cursor=mycon.cursor()
cursor.execute("drop table if exists EMPLOYEE")
cursor.execute("drop table if exists Department")
cursor.execute("create table Employee(Employee_ID int primary key not null,Employee_Name varchar(20),Date_of_join date not null,Gender char(1),Phone_number bigint not null, Aadhar_card_no char(20) not null,Email_ID varchar(30),Address text not null)")
cursor.execute("create table Department(Employee_ID int primary key not null,Department_name varchar(40) not null,Designation varchar(30),Salary int not null,No_of_projects int not null)")
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
cursor.execute("insert into Department values(1,'Production','Employee',25000,0)")
cursor.execute("insert into Department values(2,'Research and Development','Cheif developing officer',62500,2)")
cursor.execute("insert into Department values(3,'Purchasing','Cheif purchasing officer',60000,3)")
cursor.execute("insert into Department values(4,'Production','Cheif producting officer',50000,1)")
cursor.execute("insert into Department values(5,'Marketing','Cheif marketing officer',45000,2)")
cursor.execute("insert into Department values(6,'Production','Employee',29000,1)")
cursor.execute("insert into Department values(7,'HR','Cheif HR officer',65000,3)")
cursor.execute("insert into Department values(8,'Accounting and Finance','Cheif officer',70000,4)")
cursor.execute("insert into Department values(9,'Graphics and animation','Employee',28000,0)")
cursor.execute("insert into Department values(10,'Animation','Employee',30000,1)")

def all():
    cursor.execute("SELECT Employee.Employee_ID,Employee_name,Date_of_join,Gender,Department_name,Designation,Salary,No_of_projects from EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID")
    x=cursor.fetchall()
    l = ["Employee_ID", "Employee_name","Date of join","Gender", "Department_name","Designation","Salary","No_of_projects"]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    mycon.commit()

def individual():
    empid=int(input("Enter Employee_ID: "))
    cursor.execute("Select * from EMPLOYEE")
    a=cursor.fetchall()
    s=False
    for i in a:
        l=list(i)
        if i[0]==empid:
            s=True
            break
    if s:
        cursor.execute("SELECT Employee.Employee_ID,Employee_name,Date_of_join,Gender,Department_name,Designation,Salary,No_of_projects from EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID and Employee.Employee_ID={}".format(empid))
        x = cursor.fetchall()
        l = ["Employee_ID", "Employee_name", "Date of join", "Gender", "Department_name", "Designation", "Salary","No_of_projects"]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
        mycon.commit()
    else:
        print("Employee ID doesn't exist")

print("Generate Report of ")
while True:
    print("\n1. All employees \n2. Individual employee \n3. Exit")
    n=int(input("Enter your choice:"))
    if n==1:
        all()
        print()
    elif n==2:
        individual()
        print()
    elif n==3:
        break
    else:
        print("Wrong Option")
mycon.close()