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

# from main import books_data_path,users_data_path,credt_data_path,empls_data_path
from function_utils import *

books_data_path = r"C:\Users\HP\Desktop\training\Python\Books_Store_Project\books_store\books_copy.xlsx"
users_data_path = r"C:\Users\HP\Desktop\training\Python\Books_Store_Project\books_store\users_data.xlsx"
empls_data_path = r"C:\Users\HP\Desktop\training\Python\Books_Store_Project\books_store\empls_data.csv"
credt_data_path = r"C:\Users\HP\Desktop\training\Python\Books_Store_Project\books_store\credentials.txt"

#------------------------------------------------
# PROGRAM STARTS FROM HERE :
#------------------------------------------------


def add_new_employee():

    a,b,c = 0,0,0 #initialising
    while True:
        a = 0
        decor_line()
        emp_first_name = user_input("Enter first name of employee : ").lower().title()
        if not emp_first_name.isalpha():
            error_message("Please Enter Valid Name !")
        else:
            correct_message(f"First Name Verified {emp_first_name}")
            a = 1
            break

    if a == 1:
        while True:
            b = 0
            decor_line()
            emp_last_name = user_input("Enter last name of employee : ").lower().title()
            if not emp_last_name.isalpha():
                error_message(" PLease Enter Valid Name !")
            else:
                correct_message(f"Last Name Verified {emp_last_name}")
                b = 1
                break

    if b == 1:
        while True:
            c = 0
            decor_line()
            emp_mob_no = user_input("Enter Mobile Number of employee : ")

            if not emp_mob_no.isdigit() or len(emp_mob_no) != 10:
                error_message(" PLease Enter Valid Mobile Number !")

            else:
                with open(empls_data_path, "r") as f:
                    data = csv.reader(f)
                    for row in data:
                        if row[3] == emp_mob_no:
                            info_message("\nEmployee Already Registered!\n")
                            return

                correct_message(f"Phone Number Verified {emp_mob_no}")         
                info_message(f"OTP sent to mobile number : +91{emp_mob_no}\n")
                c = 1
                break

    if c == 1:
        otp = random.randint(1000, 9999)
        print("Hint : Your OTP is: ",otp)                    
        while True:
            decor_line()
            emp_otp = user_input("Enter OTP sent on employee's registered number : ")
            if emp_otp != str(otp):
                error_message(" Invalid OTP")
            else:
                correct_message(f"OTP Verified")
                d = 1
                break

    if d == 1:
        with open(empls_data_path, "r") as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                last_emp_id = row[0]

            digt = int(last_emp_id[3:]) + 1
            new_emp_id = "EMP" + str(digt)

        code = random.randint(1000, 9999)
        usecode = hashlib.md5(str(code).encode()).hexdigest()

        decor_line()
        text_color(f"Use this Employee Id & Code to create employee account --> {new_emp_id} : {code}")
        decor_line()

        with open(credt_data_path, "a") as f:
            f.write(f"{new_emp_id} {usecode}\n")

        with open(empls_data_path, "a", newline="\n") as file:
            write = csv.writer(file)
            write.writerow([new_emp_id,emp_first_name,emp_last_name,emp_mob_no])

def grant_revoke_access(result):
    """
    Function to grant/ revoke the access given by user to the employee

    """
    a,b,c,d = 0,0,0,0 # Initializing
    while True:
        decor_line()
        first_name = user_input("Enter first name of employee : ").lower().title()

        if first_name.isalpha() == True:
            correct_message(f" First Name Verified : {first_name}")
            a = 1
            break

        else:
            error_message("Please enter valid name")           

    if a == 1:
        while True:
            decor_line()
            last_name = user_input("Enter last name of employee : ").lower().title()

            if last_name.isalpha() == True:
                correct_message(f"Last Name Verified : {last_name}")
                b = 1
                break

            else:
                error_message(" Please enter valid name")

    if b == 1:
        while True:

            decor_line()
            phone_number = user_input("Enter Phone Number of employee : ")

            with open(empls_data_path, "r") as f:
                data = csv.reader(f)
                next(data)
                for row in data:
                    if str(row[3]) == phone_number:
                        pn = str(row[3])
                        c = 1
                        
                break
    if c != 1:
        error_message("Employee details not registered \n")
        return
    
    else:
        decor_line()
        correct_message(f"Phone Number Verified {pn}")
        while True : 
            decor_line()
            head_color("Available accesses that you can grant/revoke to employees : \n")
            head_color("You can grant/revoke only one access at a time : \n")
            info_message("1. Cashier")
            info_message("2. Stock Clerk")
            info_message("3. Proprietor\n")

            opt = user_input("Enter option number from above data : ")
            
            if opt == "1":
                access = "c"
                break

            if opt == "2":
                access = "s"
                break

            if opt == "3":
                access = "p"
                break

            else :
                option_error()

        with open(empls_data_path, "r+", newline="") as f:
            rows = list(csv.reader(f))

            for row in rows:
                if row[3] == pn:
                    if row and len(row) == 6 and result == "g":
                        d = 1
                        row.append(access)
                    elif row and len(row) == 7 and result == "g":
                        d = 1
                        row[6] = row[6] + access
                    elif row and len(row) == 7:
                        d =1
                        row[6] = row[6].replace(access,"")
                    elif row and len(row) == 6:
                        d = 2
                    else:
                        d = 3

            if d == 1:
                f.seek(0)
                f.truncate()
                write = csv.writer(f)
                write.writerows(rows)

            if d == 2:
                error_message("Not accessed with any applications to revoke!")
                return

            if d == 3:
                error_message("Please ensure that employee has created username & password before granting/revoking any access!")
                return

    
grant_revoke_access("g")
# add_new_employee()



