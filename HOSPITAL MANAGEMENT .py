import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
from matplotlib import style
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Wash@1234",
    database='hospitaldetail'
)
mycursor = mydb.cursor()
print('''         *******************
        **************************************
*******PROJECT ON HOSPITAL MANAGEMENT SYSTEM********
          **************************************
                 *********************''')
print('You are working in HOSPITAL MANAGEMENT SYSTEM PROJECT ')

def doctor_table():
    # to create table
    mycursor.execute("CREATE TABLE doctordetails (id int ,name VARCHAR(255),age int, department VARCHAR(255),phone int )")


def desc_doctor_details():
    print("show the structure of doctor details table ")
    df = pd.read_sql("describe  doctordetails", mydb)
    print(df)


def insert_doctor_details():
    print("Enter the details of new doctor")
    id = int(input("Enter ID of doctor: "))
    name = input("Enter doctor name: ")
    age = int(input("Enter age: "))
    department = input("Enter the department: ")
    phone = int(input("Enter phone number: "))
    sql = f"INSERT INTO doctordetails VALUES ('{id}','{name}','{age}','{department}','{phone}')"
    mycursor.execute(sql)
    print("Registred new doctor")
    mydb.commit()


def show_record_doctor_details():
    print("All record of doctors")
    df = pd.read_sql("select * from doctordetails ",mydb)
    print(df)


def create_patient_details():
    print("create table for patients")
    mycursor.execute(
        "CREATE TABLE patient_detail (id int ,name VARCHAR(255),age int, problems  VARCHAR(255),phone int(15))")
    print("table created")


def desc_patient_details():
    print("show the structure of patient details table ")
    df = pd.read_sql("describe  patient_detail", mydb)
    print(df)


def insert_patient_details():
    print("Enter new patient information")
    id = int(input("Enter ID of patient: "))
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    problems = input("Enter the problem: ")
    phone = int(input("Enter phone number: "))
    sql = f"INSERT INTO patient_detail VALUES ('{id}','{name}','{age}','{problems}','{phone}')"
    mycursor.execute(sql)
    print("succesfully registrated")
    mydb.commit()


def show_record_patient_details():
    print("Record of all patients")
    df = pd.read_sql("select * from patient_detail ",mydb)
    print(df)

def create_worker_details():
    print("create table for worker ")
    mycursor.execute(
        "CREATE TABLE worker_detail (id int ,name VARCHAR(255),age int, workname  VARCHAR(255),phone int(15))")
    print("table created")

def desc_worker_details():
    print("show the structure of worker details table ")
    df = pd.read_sql("describe  worker_detail", mydb)
    print(df)


def insert_worker_details():
    print("Enter new worker information")
    id = int(input("Enter ID of worker: "))
    name = input("Enter worker name: ")
    age = int(input("Enter age: "))
    workname = input("Enter the workname: ")
    phone = int(input("Enter phone number: "))
    sql = f"INSERT INTO worker_detail VALUES ('{id}','{name}','{age}','{workname}','{phone}')"
    mycursor.execute(sql)
    print("succesfully registrated")
    mydb.commit()


def show_record_worker_details():
    print("Record of all worker")
    df = pd.read_sql("select * from worker_detail ",mydb)
    print(df)

def search_doctor_details():
    print("Search doctor record by entering ID")
    exp = int (input("Enter doctor Id: "))
    qry = f"select * from doctordetails where id={exp}"
    df = pd.read_sql(qry, mydb)
    print(df)

def search_patient_details():
    print("Search patient record by entering ID")
    exp = float(input("Enter patient Id: "))
    qry = f"select * from patient_detail where id={exp}"
    df = pd.read_sql(qry, mydb)
    print(df)

def search_worker_details():
    print("Search doctor record by entering ID")
    exp = float(input("Enter doctor Id: "))
    qry = f"select * from worker_detail where id={exp}"
    df = pd.read_sql(qry, mydb)
    print(df)

def update_doctor_details():
    print("update details of doctor")
    department = input("enter department: ")
    id = int(input("enter ID: "))
    mycursor.execute(f"update doctorsdetails set department={department} where id={id}")
    mydb.commit()
    df = pd.read_sql("select * from  doctorsdetails", mydb)
    print(df)

def update_patient_details():
    print("change phone no. of patient")
    phone = int(input("Enter phone number: "))
    id = int(input("Enter ID: "))
    mycursor.execute(f"update patient_details set phone={phone} where id={id}")
    mydb.commit()
    df = pd.read_sql("select * from patient_details", mydb)
    print(df)

def update_worker_details():
    print("change age of worker")
    age = int(input("Enter Age: "))
    id = int(input("Enter ID: "))
    mycursor.execute(f"update worker_details set age={age} where id={id}")
    mydb.commit()
    df = pd.read_sql("select * from worker_details", mydb)
    print(df)

def create_bill_detail_table():
    mycursor.execute("CREATE TABLE bill (id int ,name VARCHAR(255),age int, drvisit int,medicine VARCHAR(255),room int)")
    print(("Bill table created"))

def insert_bill_details():
    print("Enter charge of patient in Bill")
    id = int(input("Enter ID of patient: "))
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    Dr_visit = int(input("Enter fee of Dr. visit: "))
    medicine = int(input("Enter cost of medicine: "))
    room = int(input("Enter room charge: "))
    sql = f"INSERT INTO bill VALUES ('{id}','{name}','{age}','{Dr_visit}','{medicine}','{room}')"
    mycursor.execute(sql)
    print("succesfully Biiled")
    mydb.commit()

def show_record_bill():
    print("All record of bill")
    df = pd.read_sql("select * from bill", mydb)
    print(df)



def delcolmn():
    df = pd.read_sql("select * from bill", mydb)
    print(df)
    print()
    print()
    print('column deleted')
    del df['totalbill']
    print(df)


def totalbill():
    print("Record of charge without totaling Bill")
    print()
    df = pd.read_sql("select * from bill", mydb)
    print(df)
    print()
    column_list = list(df)
    print(column_list)
    print()
    print("Record of charge with totaling Bill")
    df = pd.read_sql("SELECT *, (drvisit + medicine + room) AS totalbill  FROM bill",mydb)
    print(df)

def line_plot():
    print("line plot")
    df = pd.read_sql("select * from bill", mydb)
    x1 = df['name']
    y1 = df['drvisit']
    y2 = df['room']
    style.use("ggplot")
    plt.title('charge of name,drvisit on the items')
    plt.xlabel("Name of patients")
    plt.ylabel("Dr visit charge")
    plt.plot(x1, y1, color='r', linewidth=5, marker='o', markerfacecolor="blue",label="Dr visit charge ")
    plt.plot(x1, y2, color='g', linewidth=5, marker='o', markerfacecolor="blue",label='Room charge')
    plt.legend(loc=0)
    plt.show()

def pie_plot():
    print("pie plot")
    df = pd.read_sql("select * from bill", mydb)
    print(df)
    plt.title('charge of room,medicine,Dr. visit on the items')
    Total_Exp =eval(input("Enter charge of room,medicine,Dr visit in sq brackets:"))
    color = ['red', 'green', 'blue']
    items = ['medicine', 'room', 'Dr_visit']
    exp1 = [0, 0, 0.2]
    plt.pie(Total_Exp,colors=color, labels=items, explode=exp1, autopct='%5.1f%%')
    plt.show()

def bar_plot():
    print("Bar plot")
    df=pd.read_sql("select * from bill",mydb)
    x1=df['name']
    y1=df['medicine']
    plt.xlabel('patent name',fontsize=14,color="r")
    plt.xlabel('medicine', fontsize=14, color="r")
    plt.title("paid for madicine",fontsize=14,color='blue')
    plt.xticks(fontsize=14,rotation=30)
    plt.bar(x1,y1,width=0.5,facecolor='r',edgecolor='green')
    plt.show()



print("1.Create table of doctor_details")
print("2.Describe doctor_details")
print("3.Register doctor detail")
print("4.All doctor_details")
print("5.Create table of patient_details")
print("6.Describe patient_details")
print("7.Register patient details ")
print("8.All patient details")
print("9.Create table of worker_details")
print("10.Describe worker_details")
print("11.Register worker details ")
print("12.All worker details")
print("13.Search doctor details")
print("14.Search patient details")
print("15.Search worker details")
print("16.Update doctor details")
print("17.Update patient details")
print("18.Update worker details")
print("19.Bill details")
print("20.Enter charge of patient for Bill_details")
print("21.Show record of Bill")
print("22.Delete a column")
print("23.Total Bill")
print("24.Line plot")
print("25.pie plot")
print("26.Bar plot")


opt = int(input('Enter the option: '))
if opt == 1:
    doctor_table()
elif opt == 2:
    desc_doctor_details()
elif opt == 3:
    insert_doctor_details()
elif opt == 4:
    show_record_doctor_details()
elif opt == 5:
    create_patient_details()
elif opt == 6:
    desc_patient_details()
elif opt == 7:
    insert_patient_details()
elif opt == 8:
    show_record_patient_details()
elif opt == 9:
    create_worker_details()
elif opt == 10:
    desc_worker_details()
elif opt == 11:
    insert_worker_details()
elif opt == 12:
    show_record_worker_details()
elif opt==13:
    search_doctor_details()
elif opt==14:
    search_patient_details()
elif opt==15:
    search_worker_details()
elif opt==16:
    update_doctor_details()
elif opt==17:
    update_patient_details()
elif opt==18:
    update_worker_details()
elif opt==19:
    create_bill_detail_table()
elif opt==20:
    insert_bill_details()
elif opt==21:
    show_record_bill()
elif opt==22:
    delcolmn()
elif opt==23:
    totalbill()
elif opt==24:
    line_plot()
elif opt==25:
    pie_plot()
elif opt==26:
    bar_plot()
else:
    print("You have entered invalid option")

