import mysql.connector


mycon = mysql.connector.connect(host="localhost",user="root",password="nps123",database="project")
cursor = mycon.cursor()

dept_list = ["Production", 'Research and Development', 'Purchasing', 'Marketing', 'HR', 'Accounting and Finance',
             'Animation']

crit_list = ["Phone_number","Email_ID","Address"]

des_list = ["Employee", "Chief operating officer", "Chief developing officer", "Chief purchasing officer",
            "Chief producting officer", "Chief marketing officer", "Chief HR officer"]

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