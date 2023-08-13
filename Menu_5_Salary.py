
import mysql.connector

mycon = mysql.connector.connect(host="localhost", user="root", password="nps123", database="project")
cursor = mycon.cursor()

cursor.execute("drop table if exists Salary")
cursor.execute("create table Salary(Employee_ID int primary key ,Basic int not null,HRA int not null,DA int not null,Tax int not null,Net int not null)")


def sal_individual():
    e_id = int(input("Enter Employee ID"))
    cursor.execute("SELECT Employee_ID from EMPLOYEE ")
    x = cursor.fetchall()
    for i in x:
        if i == e_id:
            base, hra, da, tax, total = sal_add()
            cursor.execute("INSERT INTO SALARY VALUES({},{},{},{},{},{})".format(e_id, base, hra, da, tax, total))
            print("Record added successfully")
        else:
            print("Employee doesn't exist")


def sal_add():
    e_id = int(input("Enter Employee ID"))
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
            tax = int(input("Enter percentage of TAX: "))
            h = (hra / 100) * base
            d = (da / 100) * base
            t = (tax / 100) * base
            net_value = base - (d + t + h)
            cursor.execute("UPDATE Salary set Basic={} where Employee_Id={}".format(base,e_id))
            cursor.execute("UPDATE Salary set HRA={} where Employee_Id={}".format(hra,e_id))
            cursor.execute("UPDATE Salary set DA={} where Employee_Id={}".format(da,e_id))
            cursor.execute("UPDATE Salary set Tax={} where Employee_Id={}".format(tax,e_id))
            cursor.execute("UPDATE Salary set Net={} where Employee_Id={}".format(net_value,e_id))
    else:
        print("Employee Doesn't exist")



mycon.close()

