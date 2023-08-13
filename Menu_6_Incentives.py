#Incentive menu
#Input incentive rate - updating new salary in the table


import mysql.connector
import tabulate

mycon = mysql.connector.connect(host="localhost", user="root", password="nps123", database="project")
cursor = mycon.cursor()

dept_list=["Production",'Research and Development','Purchasing','Marketing','HR','Accounting and Finance','Animation']

cursor.execute("create table Incentive(Employee_ID int primary key,Incentive int default 0,Net+Incentive int)")
def default_inc():
    x=int(input("Enter incentive rate: "))
    cursor.execute("select * from Salary")
    a=cursor.fetchall()
    for i in a:
        b=x/100 * i
        c=i+b
        cursor.execute("update Incentive set Incentive={} where Employee_ID={}".format(b,i[0]))
        cursor.execute("update Incentive set Net+Incentive={} where Employee_ID={}".format(c,i[0]))
    mycon.commit()
    cursor.execute("select  Salary.Employee_Id,Basic,HRA,DA,Tax,Net,Incentive,Net+Incentive from salary,incentive where salary.Employee_ID=incentive.Employee_ID")
    x=cursor.fetchall()
    l = ["Employee_ID", "Basic", "HRA", "DA", "Tax", "Net","Incentive","Net_Incentive"]
    print(tabulate(x, headers=l, tablefmt='fancy_grid'))

def dept_inc():
    x=input("Enter the department")
    if x in dept_list:
        ic=int(input("Enter incentive rate: "))
        cursor.execute("select Salary.Employee_ID,Department_name,Net from salary,department where department='{}'".format(x))
        a=cursor.fetchall()
        for i in a:
            b=(ic*i[2])//100
            c=b+i[2]
            cursor.execute("update Incentive set Incentive={} where Employee_ID={}".format(b, i[0]))
            cursor.execute("update Incentive set Net+Incentive={} where Employee_ID={}".format(c, i[0]))
        mycon.commit()
        cursor.execute(
            "select Salary.Employee_Id,Department_name,Net,Incentive,Net_Incentive from Salary s JOIN Department d ON s.Employee_ID=d.Employee_Id JOIN Incentive e ON d.Employee_Id=e.Employee_Id")
        x = cursor.fetchall()
        l = ["Employee_ID", "Department_Name","Net", "Incentive", "Net_Incentive"]
        print(tabulate(x, headers=l, tablefmt='fancy_grid'))
    else:
        print("Department doesn't exist")

#select Salary.Employee_Id,Department_name,Net,Incentive,Net_Incentive from Salary s JOIN Department d ON s.Employee_ID=d.Employee_Id JOIN Incentive e ON d.Employee_Id=e.Employee_Id
