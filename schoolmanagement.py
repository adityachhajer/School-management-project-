"""databasename-school
table name- detail"""
import mysql.connector as np

myconn = np.connect(
    host = "localhost",
    user="root",
    password="12345",
    database="school"
)

cur=myconn.cursor()
x = 0
def passwo():
    pd=input("enter the password....:")
    if (pd=='123'):
        operatio()
    else:
        print("invalid password...try again")
        global x
        x=x+1
        if(x<3):
            passwo()
        else:
            print("\n\n you have attempted maximum limit....")
            exit()


def operatio():
    print("enter 1 to c d details...:")
    print("enter 2 to add a student...")
    print("enter 3 to remove a student...")
    print("enter 4 to update the details ...")
    print("enter 5 to see the due fees.:")
    print("enter 6 to search a particular name in school...")
    x = int(input("enter a valid number...:"))

    if (x == 1):
        details()
    elif (x == 2):
        add()
    elif (x == 3):
        remove()
    elif (x == 4):
        update()
    elif (x == 5):
        duefees()
    elif (x == 6):
        searchh()
    else:
        print("enter a valid number:")
        operatio()
    again()


def details():
    cur.execute("select * from detail;")
    t=cur.fetchall()
    for i in t:
        print("\nroll_no:-",i[0])
        print("\nname:-",i[1])
        print("\nf_name:-",i[2])
        print("\nclass:-",i[3])
        print("\nfees:-",i[4])
        print("\nmarks of 1st subject:-",i[5])
        print("\n marks of 2nd subject:-",i[6])
        print("\n marks of 3rd subject:-",i[7])
        print("\n total marks:-",i[8])
        print("*"*50)

def add():
    name=input("enter your name:")
    f_name=input("enter your father's name:")
    classs=int(input("enter the class in which you want admission:"))
    fee=int(input("fees for taking admission in this school is 20000:-"))
    '''marks1=0
    marks2=0,%s,%s,%s,%s
    marks3=0,marks1,marks2,marks3,total
    total=marks1+marks2+marks3'''
    if (fee>20000):
        ins="insert into detail(name,f_name,class,fees) values(%s,%s,%s,%s);"
        dt=(name,f_name,classs,fee)
        cur.execute(ins,dt)
        myconn.commit()
    else:
        print("fees is not paid fully.....")
    again()

def remove():
    roll_no=int(input("enter the roll no:"))
    name=input("enter the name name:")
    dell="delete from detail where roll_no=%s and name=%s;"
    upt=(roll_no,name)
    cur.execute(dell,upt)
    myconn.commit()

def update():
    print("enter 1 to update name:")
    print("enter 2 to update f_name name:")
    print("enter 3 to update class:")
    x = int(input("what changes you want..:"))
    if (x==1):
        roll_no=int(input("enter the roll_no:"))
        name=input("enter your name to be updated:")
        uppd="update detail set name=%s where roll_no=%s"
        ddt=(name,roll_no)
        cur.execute(uppd,ddt)
        myconn.commit()
    elif(x==2):
        roll_no = int(input("enter the roll_no:"))
        name = input("enter your name:")
        f_name = input("enter your f_name name to be updated:")
        uppd = "update detail set f_name=%s where roll_no=%s and name=%s"
        ddt = (f_name, roll_no,name)
        cur.execute(uppd, ddt)
        myconn.commit()
    elif (x==3):
        roll_no = int(input("enter the roll_no:"))
        name = input("enter your name:")
        classs = input("enter class to be updated:")
        uppd = "update detail set class=%s where roll_no=%s and name=%s"
        ddt = (classs, roll_no,name)
        cur.execute(uppd, ddt)
        myconn.commit()

def duefees():
    cur.execute("select * from detail where fees>20000;")
    t=cur.fetchall()
    for i in t:
        print(i)

def searchh():
    name=input("enter the name to be searched:")
    classs=int(input("in which class you want 2 search:"))
    showw="select name from detail where name=%s and class=%s;"
    det=(name,classs)
    cur.execute(showw,det)
    t=cur.fetchall()
    for a in t:
        print(a)

def again():
    ag = input("press y to do more and n to exit:")
    if ag.upper() == 'Y':
        operatio()
    elif ag.upper() == 'N':
        print("c u later")
        exit()
    else:
        print("enter valid choice")
        again()

passwo()
operatio()
again()





