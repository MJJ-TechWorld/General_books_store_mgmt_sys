#----------------    BACKEND    -----------------

#------------------------------------------------
# IMPORTANT IMPORTS FOR THIS PROGRAM
#------------------------------------------------

import csv
import random
import time
import uuid
import os
import hashlib

from getpass import getpass
from datetime import datetime, timedelta
from pyfiglet import figlet_format

from rich.console import Console
from rich.table import Table
from rich.progress import track

from main import books_data_path,users_data_path,credt_data_path,empls_data_path

#------------------------------------------------
# PROGRAM STARTS FROM HERE :
#------------------------------------------------

def create_employees_data():
    with open("empls_data_path", "a", newline="\n") as f:
        writer = csv.writer(f)
        writer.writerow(["emp id","first name","last name","phone number","use","pass","access"])

def add_new_employee():

    a,b,c = 0,0,0 #initialising
    while True:
        emp_first_name = input("Enter first name of employee : ").strip().lower().title()
        if not emp_first_name.isalpha():
            print("⚠️ Please Enter Valid Name !")
        else:
            a = 1
            break

    if a == 1:
        while True:
            emp_last_name = input("Enter last name of employee : ").strip().lower().title()
            if not emp_last_name.isalpha():
                print("⚠️ PLease Enter Valid Name !")
            else:
                b = 1
                break

    if b == 1:
        while True:
            c = 0
            emp_mob_no = input("Enter Mobile Number of employee : ").strip()
            if not emp_mob_no.isdigit() or len(emp_mob_no) != 10:
                print("⚠️ PLease Enter Valid Mobile Number !")
            else:
                print("OTP sent to mobile number : +91",emp_mob_no)
                c = 1
                break

    if c == 1:
        otp = random.randint(1000, 9999)
        print("Hint : Your OTP is: ",otp)                    
        while True:
            emp_otp = input("Enter OTP sent on employee's registered number : ")
            if emp_otp != str(otp):
                print("⚠️ Invalid OTP")
            else:
                d = 1
                break

    if d == 1:

        if not os.path.exists(empls_data_path):
            create_employees_data()

        with open(empls_data_path, "r") as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                last_emp_id = row[0]

            digt = int(last_emp_id[3:]) + 1
            new_emp_id = "EMP" + str(digt)

        code = random.randint(1000, 9999)
        usecode = hashlib.md5(str(code).encode()).hexdigest()
        print("Use this Employee Id & Code to create employee account", new_emp_id, code)

        with open(credt_data_path, "a") as f:
            f.write(f"{new_emp_id} {usecode}\n")

        if not os.path.exists(empls_data_path):
            create_employees_data()

        with open(empls_data_path, "a", newline="\n") as file:
            write = csv.writer(file)
            write.writerow([new_emp_id,emp_first_name,emp_last_name,emp_mob_no])

add_new_employee()






    
