import mysql.connector
from tabulate import tabulate

mycon = mysql.connector.connect(host="localhost", user="root", passwd="nps123", database="project")
cursor = mycon.cursor()

cursor.execute("drop table if exists EMPLOYEE")
cursor.execute("drop table if exists Department")
cursor.execute("drop table if exists Salary")
cursor.execute("drop table if exists incentive")

#cursor.execute("create table login(Username varchar(20), Password varchar(20))")
cursor.execute(
    "create table Employee(Employee_ID int primary key not null,Employee_Name varchar(20),Date_of_join date not null,Gender char(1),Phone_number bigint not null, Aadhar_card_no char(20) not null,Email_ID varchar(30),Address text not null)")
cursor.execute(
    "create table Department(Employee_ID int primary key not null,Department_name varchar(40) not null,Designation varchar(30),No_of_projects int not null)")
cursor.execute(
    "create table Salary(Employee_ID int primary key ,Basic int not null,HRA int not null,DA int not null,Tax int not null,Net int not null)")

cursor.execute("create table Incentive(Employee_ID int primary key,Incentive int default 0,Net_Incentive int)")
cursor.execute(
    "insert into Employee values(1,'Ramesh','2020/02/12','M',9860521453,'1234 4367 7890 5621','ramesh02@gmail.com','flat no 999 opendoor apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(2,'Cody','2018/03/13','M',9678902345,'7890 2376 4907 1790','codyx13@gmail.com','flat no 890 heavensgate apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(3,'Shiv','2017/10/01','M',8889576565,'6809 5780 1090 6666','shiviv70@gmail.com','flat no 303 urban apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(4,'Amy','2019/09/10','F',9900521453,'5680 9800 4589 2222','amyQ2@gmail.com','flat no 111 bluesky apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(5,'Akhila','2018/04/27','F',9645789033,'9090 6070 4566 1234','akhila70@gmail.com','flat no 903 bluesky apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(6,'Zoya','2019/03/30','F',7908974560,'9234 8378 9060 7777','ZoyaZ78@gmail.com','flat no 45 breezeway apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(7,'Akhil','2017/05/15','M',7908974590,'7890 8378 2468 7777','akhileats9@gmail.com','flat no 30 breezeway apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(8,'Nadia','2017/03/09','F',7090012345,'7640 5031 2021 2177','nads03@gmail.com','flat no 690 oceanshore apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(9,'Alvin','2020/12/01','M',8577633464,'2094 7051 9554 8967','Alvinchip4@gmail.com','flat no 01 breezeway apartments,Bangalore')")
cursor.execute(
    "insert into Employee values(10,'Andy','2019/11/08','M',9976391290,'3190 6060 8809 5678','AndyL90@gmail.com','flat no 001 millenial apartments,Bangalore')")

cursor.execute("insert into Department values(1,'Production','Employee',0)")
cursor.execute("insert into Department values(2,'Research and Development','Cheif developing officer',2)")
cursor.execute("insert into Department values(3,'Purchasing','Cheif purchasing officer',3)")
cursor.execute("insert into Department values(4,'Production','Cheif producting officer',1)")
cursor.execute("insert into Department values(5,'Marketing','Cheif marketing officer',2)")
cursor.execute("insert into Department values(6,'Production','Employee',1)")
cursor.execute("insert into Department values(7,'HR','Cheif HR officer',3)")
cursor.execute("insert into Department values(8,'Accounting and Finance','Cheif operating officer',4)")
cursor.execute("insert into Department values(9,'Accounting and Finance','Employee',0)")
cursor.execute("insert into Department values(10,'Animation','Employee',1)")

cursor.execute("insert into login values('Nitishkumar','Nitish@2810')")


cursor.execute("insert into Salary values(1, 20000, 400, 600, 1200, 17800)")
cursor.execute("insert into Salary values(2, 35000, 700, 1050, 2100, 31150)")
cursor.execute("insert into Salary values(3, 37500, 750, 1125, 2250, 33375)")
cursor.execute("insert into Salary values(4, 40000, 800, 1200, 2400, 35600)")
cursor.execute("insert into Salary values(5, 33000, 660, 990, 1980, 29370)")
cursor.execute("insert into Salary values(6, 22000, 440, 660, 1320, 19580)")
cursor.execute("insert into Salary values(7, 45000, 900, 1350, 2700, 40050)")
cursor.execute("insert into Salary values(8, 30000, 600, 900, 1800, 26700)")
cursor.execute("insert into Salary values(9, 24000, 480, 720, 1440, 21360)")
cursor.execute("insert into Salary values(10, 25000, 500, 750, 1500, 22250)")

cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(1,18000)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(2,31500)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(3,33750)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(4,36000)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(5,29700)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(6,19800)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(7,40500)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(8,27000)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(9,21600)")
cursor.execute("Insert into incentive(Employee_ID,Net_Incentive) values(10,22500)")
cursor.close()

des_list = ["Employee", "Chief operating officer", "Chief developing officer", "Chief purchasing officer",
            "Chief producting officer", "Chief marketing officer", "Chief HR officer"]

dept_list = ["Production", 'Research and Development', 'Purchasing', 'Marketing', 'HR', 'Accounting and Finance',
             'Animation']

crit_list = ["Phone_number","Email_ID","Address"]

def welcome():
    print("                                            PAYROLL MANAGEMENT SYSTEM                     ")
    print("                                                    WELCOME USER                           ")


def sign_up():
    user = input("Enter New Username: ")
    x = login_chk(user)
    if x:
        print("Enter New password [Must contain characters, digits, special character (Minimum length 8) ] : ")
        passw = input()
        if user == passw:
            print("Username and password cannot be same\nPlease try again")
            sign_up()
        elif len(passw) >= 8:
            checked = password_checker(passw)
            conf = input("Re-enter new password: ")
            final = confirm(conf, checked)
            cursor.execute("insert into login values('{}','{}')".format(user, final))
        elif len(passw) < 8:
            print("Minimum password length must be 8 characters!")
            new_passw = retry()
            checked = password_checker(new_passw)
            conf = input("Re-enter new password: ")
            new_one = confirm(conf, checked)
            cursor.execute("insert into login values('{}','{}')".format(user, new_one))
        print("Signup Successful")
        mycon.commit()


def login_chk(user):
    cursor.execute("Select * from login")
    x=cursor.fetchall()
    for i in x:
        if i[0]==user:
            print("Username already exist!")
            print("Try logging in!")
            print()
            print("                                       Login Page                                              ")
            login()
            return False
    else:
        return True

def retry():
    print("Try Again!")
    passw = input("Enter New password: ")
    return passw

def retry2():
    print("Try Again!")
    passw = input("Enter New password: ")
    check1 = password_checker(passw)
    return check1

def confirm(conf, checked):
    if checked == conf:
        return conf
    else:
        print("Both passwords don't match")
        try1 = retry2()
        redo = input("Re-enter new password: ")
        a = confirm(try1, redo)
        return a

def password_checker(passw):
    count_alpha = 0
    count_digit = 0
    count_special = 0
    for i in passw:
        if i.isalpha():
            count_alpha += 1
        elif i.isdigit():
            count_digit += 1
        else:
            count_special += 1
    if count_alpha >= 4 and count_digit >= 1 and count_special >= 1:
        return passw
    else:
        print("Password must contain atleast 4 letters,1 digit and 1 special character!")
        new_passw = retry()
        new = password_checker(new_passw)
        return new

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    cursor.execute("select * from login")
    s = False
    data = cursor.fetchone()
    while data != None:
        l = list(data)
        if l[0] == username and l[1] == password:
            s = True
            break
        data = cursor.fetchone()
    if s:
        print("Login successful\n")
        all_menus()
        print("Thank You", "\U0001f600")

    else:
        print("Wrong username and password!")


def add():
    while True:
        print()
        print(
            "                                            EMPLOYEE GENERAL DETAILS                                    ")
        emp_id = int(input("\nEnter Employee ID: "))
        emp_name = input("Enter Employee Name: ")
        doj = input("Enter Date of Join(YYYY/MM/DD): ")
        gen = input("Enter Gender(M/F): ")
        phno = int(input("Enter Phone Number: "))
        adhr = input("Enter Aadhar card no: ")
        email = input("Enter Email ID: ")
        addres = input("Enter Employee Address: ")
        cursor = mycon.cursor(buffered=True)
        cursor.execute(
            "INSERT INTO EMPLOYEE VALUES({},'{}','{}','{}',{},'{}','{}','{}') ".format(emp_id, emp_name, doj, gen, phno,
                                                                                       adhr, email, addres))
        cursor.execute("select * from employee where Employee_ID={}".format(emp_id, ))
        x = cursor.fetchall()
        print("\nThe Employee Primary details are: ")
        l = ["Employee ID", "Employee_name", "Date_of_join", "Gender", "Phone_number", "Aadhar_card_no", "Email_Id",
             "Address"]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
        print(
            "\n                                           EMPLOYEE DEPARTMENT DETAILS                                     ")
        depart = input("\nEnter employee department: ")
        if depart not in dept_list:
            dept_list.append(depart)
        des = input("Enter employee designation: ")
        if des not in des_list:
            des_list.append(des)
        nop = int(input("Enter employee working projects: "))
        cursor.execute("INSERT INTO DEPARTMENT VALUES({},'{}','{}',{})".format(emp_id, depart, des, nop))
        cursor.execute("select * from department where Employee_ID={}".format(emp_id))
        a = cursor.fetchall()
        mycon.commit()
        print("\nThe Employee Department details are: ")
        d = ["Employee ID", "Department", "Designation", "No of Projects"]
        print(tabulate(a, headers=d, tablefmt='fancy_grid'))
        print()
        print("                                              EMPLOYEE SALARY DETAILS                                          ")
        print()
        base = int(input("Enter Basic Salary: "))
        hr = int(input("Enter percentage of HRA: "))
        daa = int(input("Enter percentage of DA: "))
        if base<50000:
            ta=6
        else:
            ta=12
        h = (hr / 100) * base
        d = (daa / 100) * base
        t = (ta / 100) * base
        net_value = base - (d + t + h)
        cursor.execute("insert into Salary values({},{},{},{},{},{})".format(emp_id, base, h, d, t, net_value))
        cursor.execute("select * from salary where Employee_ID={}".format(emp_id))
        x = cursor.fetchall()
        print("\nThe Employee salary details are: ")
        l = ["Employee_ID", "Basic", "HR", "DA", "Tax", "Net"]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
        cursor.execute("insert into incentive values({},{},{})".format(emp_id, 0, net_value))
        cursor.close()
        mycon.commit()
        print()
        print("Details of employee have been inserted successfully")
        ch = input("\nWould you like to continue(y/n): ")
        print()
        if ch == "n":
            break


def delete():
    id = int(input("Enter Employee ID to delete record: "))
    cursor.execute("Select * from EMPLOYEE")
    a = cursor.fetchall()
    s = False
    for i in a:
        if i[0] == id:
            s = True
            break
    if s:
        cursor.execute("select * from department where Employee_ID={}".format(id, ))
        a = cursor.fetchall()
        cursor.execute("select * from employee where Employee_ID={}".format(id, ))
        p = cursor.fetchall()
        cursor.execute("select * from Salary where Employee_ID={}".format(id, ))
        z = cursor.fetchall()
        print("\nThe deleted record is: ")
        l = ["Employee ID", "Employee_name", "Date_of_join", "Gender", "Phone_number", "Aadhar_card_no", "Email_Id",
             "Address"]
        print(tabulate(p, headers=l, tablefmt='fancy_grid'))
        d = ["Employee ID", "Department", "Designation", "No_of_Projects"]
        print(tabulate(a, headers=d, tablefmt='fancy_grid'))
        e = ["Employee ID", "Basic", "HRA", "DA", "Tax", "Net"]
        print(tabulate(z, headers=e, tablefmt='fancy_grid'))
        cursor.execute("DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID={}".format(id, ))
        cursor.execute("DELETE FROM DEPARTMENT WHERE Employee_ID={}".format(id, ))
        cursor.execute("DELETE FROM Salary WHERE Employee_ID={}".format(id, ))
        cursor.execute("DELETE FROM Incentive WHERE Employee_ID={}".format(id, ))
        mycon.commit()
        print("\nRecord deleted successfully\n")
    else:
        print("Employee doesn't exist")


def update_dept():
    print("\nUpdate details of: ")
    print("1. Department \n2. Designation ")
    choice = int(input("Enter criteria to be updated: "))
    eid = int(input("Enter Employee_ID to update: "))
    cursor.execute("Select * from department")
    s = False
    data = cursor.fetchone()
    while data != None:
        l = list(data)
        if l[0] == eid:
            s = True
            break
        data = cursor.fetchone()
    if s == True:
        if choice == 1:
            print("\nDepartments existing are: ")
            for i in dept_list:
                print(i)
            print()
            up_dept = input("Enter New Department Name to be updated: ")
            cursor.execute("UPDATE DEPARTMENT SET Department_Name='{}' where Employee_ID={}".format(up_dept, eid))
            print("Department set to", up_dept, "for Employee_ID", eid)
            print()
        elif choice == 2:
            print("\nDesignations existing are:")
            for i in des_list:
                print(i)
            print()
            up_desig = input("Enter New Designation to be updated: ")
            cursor.execute("UPDATE DEPARTMENT SET Designation='{}' where Employee_ID={}".format(up_desig, eid))
            print("Designation set to ", up_desig, "for Employee_ID", eid)
            print()
        else:
            print("Criteria Incorrect")
    else:
        print("Employee ID doesn't exists")
    print()

def update_emp():
    print("Criterias existing are ")
    for i in crit_list:
        print(i)
    print()
    crit = input("Enter criteria to be updated: ")
    id = int(input("Enter Employee_ID to be updated: "))
    cursor.execute("select * from EMPLOYEE")
    s = False
    data = cursor.fetchone()
    while data != None:
        l = list(data)
        if l[0] == id:
            s = True
            break
        data = cursor.fetchone()
    if s == True:
        newcrit = input("Enter new information to be updated: ")
        if crit == "Phone_number":
            cursor.execute("UPDATE EMPLOYEE SET Phone_number={} where Employee_ID={}".format(newcrit, id))
            print(crit, "of the employee has been updated to", newcrit)

        else:
            cursor.execute("UPDATE EMPLOYEE SET {}='{}' where Employee_ID={}".format(crit, newcrit, id))
            print(crit, "of the employee has been updated to", newcrit)

    else:
        print("Wrong option")
    print()

def desig():
    print("Designations existing are")
    for i in des_list:
        print(i)
    print()
    des = input("Enter Designation: ")
    cursor.execute(
        "SELECT Employee.Employee_ID, Employee_name, Designation FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID and Designation='{}' ".format(
            des, ))
    x = cursor.fetchall()
    l = ["Employee_ID", "Employee_name", "Designation"]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    mycon.commit()


def dept():
    print("Departments existing are:")
    for i in dept_list:
        print(i)
    print()
    dep = input("Enter Department: ")
    cursor.execute(
        "SELECT Employee.Employee_ID, Employee_name, Department_name FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID and Department_name='{}'".format(
            dep))
    x = cursor.fetchall()
    l = ["Employee_ID", "Employee_name", "Department_name"]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    mycon.commit()


def salary():
    print("Order salary from:\n1. Low to High\n2. High to Low\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        cursor.execute(
            "SELECT Employee.Employee_ID, Employee_name, Basic FROM EMPLOYEE, SALARY WHERE EMPLOYEE.Employee_ID=Salary.Employee_ID ORDER BY Basic")
    else:
        cursor.execute(
            "SELECT Employee.Employee_ID, Employee_name, Basic FROM EMPLOYEE, SALARY WHERE EMPLOYEE.Employee_ID=Salary.Employee_ID ORDER BY Basic desc")
    x = cursor.fetchall()
    l = ["Employee_ID", "Employee_name", "Salary"]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))
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
    l = ["Employee_ID", "Employee_name", "No_of_projects" ]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    mycon.commit()


def all():
    cursor.execute(
        "SELECT Employee.Employee_ID,Employee_name,Date_of_join,Gender,Department_name,Designation,No_of_projects from EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Employee_ID=DEPARTMENT.Employee_ID")
    x = cursor.fetchall()
    l = ["Employee_ID", "Employee_name", "Date of join", "Gender", "Department_name", "Designation",
         "No_of_projects"]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    mycon.commit()


def individual():
    print("1. Employee personal details \n2. Employee office details")
    ch = int(input("\nEnter your option: "))
    empid = int(input("Enter Employee_ID: "))
    cursor.execute("Select * from EMPLOYEE")
    a = cursor.fetchall()
    s = False
    for i in a:
        if i[0] == empid:
            s = True
            break
    if s:
        if ch == 1:
            cursor.execute("SELECT * FROM EMPLOYEE WHERE Employee_ID={}".format(empid))
            x = cursor.fetchall()
            l = ["Employee_ID", "Employee_name", "Date_of_join", "Gender", "Phone_number", "Aadhar_card", "Email_ID",
                 "Address"]
            print(tabulate(x, headers=l, tablefmt='fancy_grid'))
            mycon.commit()
        elif ch == 2:
            cursor.execute(
                "SELECT Employee.Employee_Id,Employee_name,Department_name,Designation,No_of_projects FROM Employee,Department WHERE Employee.Employee_ID=Department.Employee_ID and Employee.Employee_ID={}".format(
                    empid))
            x = cursor.fetchall()
            l = ["Employee_ID", "Employee_name", "Department", "Designation", "No_of_Projects"]
            print(tabulate(x, headers=l, tablefmt='fancy_grid'))
            mycon.commit()
    else:
        print("Employee ID doesn't exist")


def sal_add():
    e_id = int(input("Enter Employee ID: "))
    cursor.execute("SELECT Employee_ID from EMPLOYEE ")
    x = cursor.fetchall()
    s = False
    for i in x:
        if i[0] == e_id:
            s = True
            break

    if s:
        base = int(input("Enter employee basic salary: "))
        hra = int(input("Enter percentage of HRA: "))
        da = int(input("Enter percentage of DA: "))
        if base<50000:
            tax=6
        else:
            tax=12
        h = (hra / 100) * base
        d = (da / 100) * base
        t = (tax / 100) * base
        net_value = base - (d + t + h)
        cursor.execute("UPDATE Salary set Basic={} where Employee_Id={}".format(base, e_id))
        cursor.execute("UPDATE Salary set HRA={} where Employee_Id={}".format(h, e_id))
        cursor.execute("UPDATE Salary set DA={} where Employee_Id={}".format(d, e_id))
        cursor.execute("UPDATE Salary set Tax={} where Employee_Id={}".format(t, e_id))
        cursor.execute("UPDATE Salary set Net={} where Employee_Id={}".format(net_value, e_id))
        cursor.execute("select * from salary where Employee_ID={}".format(e_id))
        x = cursor.fetchall()
        l = ["Employee_ID", "Basic", "HR", "DA", "Tax", "Net"]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    else:
        print("Employee Doesn't exist")


def default_inc():
    x = int(input("Enter incentive rate: "))
    cursor.execute("select Employee_Id,Net from Salary")
    a = cursor.fetchall()
    for i in a:
        b = (x * i[1]) // 100
        c = i[1] + b
        cursor.execute("update Incentive set Incentive={} where Employee_ID={}".format(b, i[0]))
        cursor.execute("update Incentive set Net_Incentive={} where Employee_ID={}".format(c, i[0]))

    cursor.execute(
        "select  Salary.Employee_Id,Basic,HRA,DA,Tax,Net,Incentive,Net_Incentive from salary,incentive where salary.Employee_ID=incentive.Employee_ID")
    x = cursor.fetchall()
    l = ["Employee_ID", "Basic", "HR", "DA", "Tax", "Net", "Incentive", "Net_Incentive"]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))


def dept_inc():
    x = input("Enter the department: ")
    if x in dept_list:
        ic = int(input("Enter incentive rate: "))
        cursor.execute(
            "select Department.Employee_ID,Department_name,Net from salary,department where department_name='{}' and Department.Employee_ID=Salary.Employee_ID".format(
                x))
        a = cursor.fetchall()
        for i in a:
            b = (ic * i[2]) / 100
            c = b + float(i[2])
            cursor.execute("update Incentive set Incentive={} where Employee_ID={}".format(b, i[0]))
            cursor.execute("update Incentive set Net_Incentive={} where Employee_ID={}".format(c, i[0]))
        mycon.commit()
        cursor.execute(
            "select Department_name,Net,Incentive,Net_Incentive from Salary s JOIN Department d ON s.Employee_ID=d.Employee_Id JOIN Incentive e ON d.Employee_Id=e.Employee_Id where Department_name='{}'".format(
                x))
        x = cursor.fetchall()
        l = ["Department_Name", "Net", "Incentive", "Net_Incentive"]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    else:
        print("Department doesn't exist")


def menu1():
    while True:
        print("1. Add Record(s) \n2. Delete Record \n3. Return to main menu\n")
        n = int(input("Enter your choice: "))
        if n == 1:
            add()
            print("Record(s) added successfully\n")
        elif n == 2:
            delete()
            print()
        elif n == 3:
            break
        else:
            print("Wrong option")


def menu2():
    while True:
        print("1. Update Employee Details\n2. Update Department Details\n3. Return to main menu")
        chi = int(input("\nEnter choice of updation: "))
        print()
        if chi == 1:
            update_emp()
        elif chi == 2:
            update_dept()
        elif chi == 3:
            break
        else:
            print("Wrong Option")


def menu3():
    while True:
        print(
            "View Employee Details based on given criteria:\n1. Designation\n2. Department\n3. Salary\n4. No of projects\n5. Return to Main Menu\n")
        n = int(input("Enter your choice: "))
        if n == 1:
            print("\nEmployee Details Based On Designation:\n")
            desig()
            print()
        elif n == 2:
            print("\nEmployee Details Based On Department:\n")
            dept()
            print()
        elif n == 3:
            print("\nEmployee Details Based On Salary:\n")
            salary()
            print()
        elif n == 4:
            print('\nEmployee Details Based On No of projects')
            proj()
            print()
        elif n == 5:
            break
        else:
            print("Wrong option")


def menu4():
    print("Generate Report of ")
    while True:
        print("\n1. All Employees \n2. Individual Employee \n3. Return to main menu")
        n = int(input("\nEnter your choice:"))
        if n == 1:
            all()
            print()
        elif n == 2:
            individual()
            print()
        elif n == 3:
            break
        else:
            print("Wrong Option")


def menu5():
    while True:
        cursor.execute("select * from salary")
        x = cursor.fetchall()
        l = ["Employee_ID", "Basic", "HR", "DA", "Tax", "Net"]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
        print()
        print(
            "                                               UPDATE SALARY                                            ")
        sal_add()
        ch = input("Would you like to continue(y/n): ")
        if ch == "n":
            break


def menu6():
    while True:
        print("1. Default Incentive\n2. Department Based Incentive\n3. Return to main menu\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            default_inc()
            print()
        elif ch == 2:
            print("Departments existing are")
            for i in dept_list:
                print(i)
            print()
            dept_inc()
            print()
        elif ch == 3:
            print()
            break
        else:
            print("Wrong option")

def all_menus():
    while True:
        print(
            "1. ADD or Delete Employee\n2. Update Employee Details \n3. View Employee Details\n4. Generate report for Employees\n5. Update Salary\n6. Incentives\n7. Logout")
        ch = int(input("\nEnter your option: "))
        print()
        if ch == 1:
            menu1()
            print()
        elif ch == 2:
            menu2()
            print()
        elif ch == 3:
            menu3()
            print()
        elif ch == 4:
            menu4()
            print()
        elif ch == 5:
            menu5()
            print()
        elif ch == 6:
            menu6()
            print()
        elif ch == 7:
            break
        else:
            print("Wrong option")


welcome()
while True:
    cursor = mycon.cursor(buffered=True)
    print("1. Login\n2. Sign Up\n")
    n = int(input("Enter your choice: "))
    print()
    if n == 1:
        print("                                       Login Page                                              ")
        print()
        login()
        break
    elif n == 2:
        print("                                       Sign UP Page                                            ")
        sign_up()
        print()
        print("                                       Login Page:                                             ")
        login()
        break
    else:
        print("Wrong option")
        break
    cursor.close()

mycon.close()
