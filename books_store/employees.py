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

from main import books_data_path,users_data_path,empls_data_path,credt_data_path
from function_utils import *
#------------------------------------------------
# PROGRAM STARTS FROM HERE :
#------------------------------------------------


credt_data_path = r"C:\Users\HP\Desktop\training\Python\Books_Store_Project\books_store\credentials.txt"


with open(credt_data_path, "r") as f:
    data_list = f.readlines()
    f.seek(0)
    data_str = f.read()

while True:    
    decor_line()
    emp_id = user_input("Enter Your Employee Id : ").upper()
    a = 0
    for i in range(1, len(data_list)):
        if emp_id == data_list[i][:6]:
            a = 1
            break

    if a == 1:
        break 
    else:
        error_message(" Invalid Employee Id!")

while True:
    decor_line()
    emp_mob_no = user_input("Enter your registered mobile number : ")
    if not emp_mob_no.isdigit() or len(emp_mob_no) != 10:
        error_message(" PLease Enter Valid Mobile Number !")
    else:
        break

while True:
    decor_line()
    code = user_input("Enter Code to create employee account : ")
    usecode = hashlib.md5(str(code).encode()).hexdigest()
    b = 0
    code_pos = data_str.find(emp_id) + 7
    actual_code = data_str[code_pos:code_pos + 32]
    if actual_code == usecode:
        b = 1
        break
    else:
        error_message("Invalid Code")

while True:
    decor_line()
    username = user_input("Create new username : ")
    c = 0
    if username == "":
        error_message("Invalid Username")

    else:
        c = 1
        break

while True:
    decor_line()
    info_message("Password should contain 8 characters only\n")
    d = 0
    password = user_input("Enter your password : ")
    if len(password) != 8 or password == "":
        error_message("Invalid Password")
    else:
        d = 1
        break

if a == 1 and b == 1 and c == 1 and d == 1:
    with open(empls_data_path, "r+", newline="") as f:
        data = csv.reader(f)
        rows = []
        for row in data:
            if row[0] == emp_id and row[3] == emp_mob_no:
                fn,ln,pn = row[1],row[2],row[3]
                rows.append(row)

        f.seek(0)
        writer = csv.writer(f)
        writer.writerows(rows)

    progress_bar("Creating employee account")
    decor_line()
    correct_message("Account Created Successfully !")
    decor_line()