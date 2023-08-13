
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",password="nps123",database="project")
cursor=mycon.cursor()

def welcome():
    print("                                            PAYROLL MANAGEMENT SYSTEM                     ")
    print("                                                    WELCOME USER                           ")

def sign_up():
    user=input("Enter New Username:")
    print("Enter New password [Must contain characters, digits, special character (Minimum length 8) ] : ")
    passw = input()
    if user==passw:
        print("Username and password cannot be same\nPlease try again")
        sign_up()
    elif len(passw) >= 8:
        checked=password_checker(passw)
        conf=input("Re-enter new password")
        final=confirm(conf,checked)
        cursor.execute("insert into login values('{}','{}')".format(user, final))
    elif len(passw)<8:
        print("Minimum password length must be 8 characters")
        new_passw=retry()
        checked = password_checker(new_passw)
        conf = input("Re-enter new password")
        new_one = confirm(conf, checked)
        cursor.execute("insert into login values('{}','{}')".format(user, new_one))
    print("Signup Successful")
    mycon.commit()

def retry():
    print("Try Again")
    passw=input("Enter New password")
    return passw

def retry2():
    print("Try Again")
    passw = input("Enter New password")
    check1=password_checker(passw)
    return check1


def confirm(conf,checked):
    if checked==conf:
        return conf
    else:
        print("Both passwords don't match")
        try1=retry2()
        redo=input("Re-enter new password")
        a=confirm(try1,redo)
        return a

def password_checker(passw):
        count_alpha=0
        count_digit=0
        count_special=0
        for i in passw:
            if i.isalpha():
                count_alpha+=1
            elif i.isdigit():
                count_digit+=1
            else:
                count_special+=1
        if count_alpha>=4 and count_digit>=1 and count_special>=1:
            return passw
        else:
            print("Password must contain atleast 1 digit and 1 special character")
            new_passw = retry()
            new=password_checker(new_passw)
            return new

def login():
    username=input("Enter Username")
    password=input("Enter Password")
    cursor.execute("select * from login")
    s=False
    data=cursor.fetchone()
    while data!=None:
        l=list(data)
        if l[0]==username and l[1]==password:
           s=True
           break
        data = cursor.fetchone()
    if s:
        print("Login successful")
        welcome()
    else:
        print("Wrong username and password")

while True:
    welcome()
    print("1.Login\n2.Sign Up")
    n=int(input("Enter your choice"))
    if n==1:
        print("                                       Login Page                                              ")
        login()
    elif n==2:
        print("                                       Sign UP Page                                            ")
        sign_up()
        print("                                       Login Page:                                             ")
        login()
    else:
        print("Wrong option")
