#----------------    BACKEND    -----------------

import csv
import random
import time
import os
import pwinput
import openpyxl
import hashlib

from openpyxl import load_workbook
from openpyxl.styles import Alignment,Font,Border,Side
from rich import console
from datetime import datetime
from pyfiglet import figlet_format
from pyfiglet import Figlet
from rich.console import Console,Group
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.rule import Rule
from rich import box
from rich.panel import Panel
from rich.progress import track
console = Console()
from function_utils import *

#------------------------------------------------
# ASSIGNING IMP PATHS TO THE VARIABLES
#------------------------------------------------

CREDaT_DATA_PATH = "Credential.txt"
EMPLaS_DATA_PATH = "Employees_Data.csv"
BOOK_DATA_PATH = "BOOKS_DATA.xlsx"
STORE_DATA_PATH = "STORE_RECORDS.xlsx"

CREDT_DATA_PATH = "CREDENTIAL.txt"
EMPLS_DATA_PATH = "EMPLOYEES.csv"
LOG_DATA_PATH = "Activity_Log.txt"


#------------------------------------------------
# PROGRAM START FROM HERE :
#------------------------------------------------

# DEFINING IMP FUNCTIONS USED IN THIS PROGRAM ---


def main_menu(title):

    create_imp_files()
    menu_title(title)
    head_color("What would you like to do ?\n")
    info_message("\t1. Create Employee Account -")
    info_message("\t2. Order Processing-")
    info_message("\t3. Stock Audit -")
    info_message("\t4. Enterprise Management -")
    info_message("\t5. Exit -")

    while True:
        decor_line()    
        select_option = user_input("Enter option number from options : ")

        if select_option == "1":
            first_p()
            main_menu("MAIN PORTAL")
            break

        elif select_option == "2":
            login_portal("c")
            second_p()
            main_menu("MAIN PORTAL")
            break

        elif select_option == "3":
            login_portal("s")
            third_p()
            main_menu("MAIN PORTAL")
            break

        elif select_option == "4":
            login_portal("p")
            fourth_p()
            main_menu("MAIN PORTAL")
            break

        elif select_option == "5":
            return
        
        else:
            option_error()

def first_p():

    sub_title("EMPLOYEES CORNER")

    def create_account():

        head_color("\n--- Create New Employee Account ---\n")

        with open(CREDT_DATA_PATH, "r") as f:
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
            with open(EMPLS_DATA_PATH, "r+", newline="") as f:
                data = csv.reader(f)
                rows = []
                for row in data:

                    if row[0] == emp_id and row[3] == emp_mob_no and len(row) == 4:
                        row.append(username)
                        row.append(password)

                    else:
                        error_message("Account Already Exists!")
                        return

                    rows.append(row)

                f.seek(0)
                writer = csv.writer(f)
                for r in rows:
                    writer.writerow(r)

                f.truncate()

            progress_bar("Creating employee account")
            decor_line()
            correct_message("Account Created Successfully !")
            decor_line()
            return
    def menu():
        head_color("What would you like to do ?\n")
        info_message("\t1. Create Employee Account -")
        info_message("\t2. Exit-")
        
        while True:
            decor_line()    
            select_option = user_input("Enter option number from options : ")

            if select_option == "1":
                create_account()
                menu()
                break
                
            elif select_option == "2":
                return

            else:
                option_error()
    menu()

def second_p():

    sub_title("CASHIER CORNER")

    def create_bill(code,bookname,author,price,quantity,total,date):

        good_quotes = ["'Books are uniquely portable magic'",
                    "'Today a reader,tomorrow a leader'",
                    "'Read what you love until you love to read'"
                    "'There is no friend as loyal as a book'",
                    "'A book dream is a dream that you hold in your hand'"]
        quote = random.choice(good_quotes)

        Total = 0
        for i in total:
            Total = Total + int(i)
        decor_line()
        title_box = Table(box=box.ROUNDED, border_style="#FFF3E0",style="on #2d1f0f",expand=True,show_header=False,padding=(1,1))
        title_box.add_column(justify="center")
        title_box.add_row(Text("📚   DIGITAL LIBRARY OF NAVI MUMBAI   📚",style="#0066FF",justify="center"))
        title_box.add_row(Text("( 🌏 💻  By MJJ-TechWorld  💻 🌏 )",style="bold #FFD700 on #1a1a1a",justify="center"))

        table = Table(box=box.DOUBLE_EDGE,
                    title_style="bold yellow",
                    header_style="bold white on blue",
                    border_style="bright_yellow",
                    show_lines=True,
                    expand=True)
        for col in ["Sr.","Unique Code","Name Of Books","Author Name", "Price","Quantity","Total"]:
            table.add_column(col,justify="center",style="cyan",overflow="fold")

        for i in range(len(code)):
            table.add_row(str(i+1),str(code[i]),str(bookname[i]),str(author[i]),str(price[i]),str(quantity[i]),str(total[i]))

        content = Group(
            title_box,
            line("bright_cyan"),
            line("bright_magenta"),
            Text(f"Date : {date}", style="cyan", justify="right"),
            table,
            Text(f"Total : Rs.{Total}/-", style="bold green", justify="right"),
            line("bright_magenta"),
            Text("--- Thank You Visit Again ---", style="bold green", justify="center"),
            line("bright_magenta"),
            Text(f"{quote}", style="bold yellow", justify="center"),
            line("bright_magenta")
            )
        console.print(Panel(content, box=box.DOUBLE, border_style="#00BFFF on #0F2D2E",padding=(1,1), width=console.width - 2),"\n")

    def buy_book():
        code_list,bookname_list,author_list,price_list,quantity_list,total_list = [],[],[],[],[],[]
        date = datetime.today().strftime('%d-%m-%Y')
        while True:
            value = False
            decor_line()
            head_color("---Buy Book(s)---\n")
            uc = user_input("Enter Unique Code Of Book : ").upper()
            wb = load_workbook(BOOK_DATA_PATH)
            for sheet in wb.sheetnames:
                s = wb[sheet]
                for row in s.iter_rows(min_row=2,values_only=True):
                    if uc == str(row[1]).strip():
                        correct_message(f"{row[2]} : By {row[3]} : Rs.{row[7]} : Avail. {row[9]}\n")
                        avail_q = row[9]
                        bookname = row[2]
                        author = row[3]
                        price = row[7]
                        value = True

            if not value:
                error_message("Book Not Found!") 
                continue

            while True:
                quantity = user_input("Enter quantity of this book : ")

                if quantity == "":
                    error_message("Quantity cannot be none!")
                    break

                if not quantity.isdigit():
                    error_message("Please enter valid quantity")
                    continue

                if int(quantity) < 0:
                    error_message("Please enter valid quantity!")
                    continue

                if int(quantity) <= int(avail_q):
                    correct_message("Book Sold Successfully!")

                    code_list.append(uc)
                    bookname_list.append(bookname)
                    author_list.append(author)
                    price_list.append(price)
                    quantity_list.append(quantity)
                    total_list.append(int(price)*int(quantity))
                    
                    wb = load_workbook(BOOK_DATA_PATH)
                    for sheet in wb.sheetnames:
                        s = wb[sheet]
                        for row in s.iter_rows(min_row=2,values_only=False):
                            if row[1].value == uc:
                                row[9].value = int(row[9].value) - int(quantity)
                    wb.save(BOOK_DATA_PATH)
                    break

                else:
                    error_message("Insufficient quantity of book available!")
                    continue

            while True:
                head_color("Want to buy more book(s)?\n")
                text_color("\t1.Yes")
                text_color("\t2.No")

                sel_option = ask_option_number()

                if sel_option == "1":
                    break

                elif sel_option == "2":
                    update_record(0,code_list,bookname_list,author_list,price_list,quantity_list,total_list,date)
                    create_bill(code_list,bookname_list,author_list,price_list,quantity_list,total_list,date)
                    return

                else:
                    option_error()
                    continue
        
    def choose_option():
        while True:
            decor_line()
            head_color("Available Options :\n")

            info_message("\t1. Want to check unique code of book once ?")
            info_message("\t2. Buy book(s) directly\n")

            sel_option = user_input("Enter option number to proceed further : ")

            if sel_option == "1":
                search_book()
                choose_option()
                menu()
                return

            elif sel_option == "2":
                buy_book()
                menu()
                return
            else:
                error_message("Please enter valid option number from given options!")


    def banner():
        f = Figlet(font='small',width=200)
        name = figlet_format('Digital Books\n Store',font="mini", width=200).strip()
        content = Group(
            Align.center(Text(name, style="bold bright_white on #00ACC1")),
            Text(""),
            Align.center(f.renderText("Digital Books Store"))
        )
        title_box = Panel(content,
                        box=box.ROUNDED,
                        border_style="#FF8C00",
                        style="on #2d1f0f",
                        padding=(1,2),
                        expand=False)

        banner_console = Console(width=120)
        banner_console.print(title_box)

        console.print(Panel(
            f"{name}\n[bold #FFD700 on #3a3200]  (By MJJ-TechWorld)  [/]",
            box=box.ROUNDED,
            border_style="#FF8C00",
            style="bold #B2EBF2 on #00363A",
            padding=(1, 3),
            expand=False
        ))


    def menu():
        decor_line()
        head_color("Actions Available :\n")
        text_color("\t1. Search book(s)")
        text_color("\t2. Buy book(s)")
        text_color("\t3. Exit")

        while True:
            decor_line()    
            select_option = user_input("Enter option number from options : ")

            if select_option == "1":
                search_book()
                menu()
                break
            elif select_option == "2":
                choose_option()
                menu()
                break

            elif select_option == "3":
                break

            else:
                option_error()

    menu()

def third_p():

    sub_title("STOCK CLERK CORNER")

    def add_new_book(result = ""):

        if result == "new":

            head_color("\n--- Add New Genre ---\n")

            genre = user_input(f"Enter genre of {result} book : ").upper()
            decor_line()

            text_color("Add atleast one book's details under this new genre\n")

            new_code = user_input("Enter general unique code for books under this genre (ex. MYTH, NOV) : ").upper()
            decor_line()
                    
            bookname = user_input(f"Enter proper name of {result} book : ")
            decor_line()

            authorname = user_input(f"Enter author name of {result} book : ")
            decor_line()
        
            lang = user_input(f"Enter language in which {result} book is written : ").upper()
            decor_line()

            publish_date = user_input(f"Enter publish date of {result} book in format 'dd-mm-yy': ")
            decor_line()

            while True:
                buy_price = user_input(f"Enter price of {result} book : ")
                decor_line()

                if buy_price.isdigit() and int(buy_price) < 0:
                    error_message("Please enter valid price !")
                else:
                    break

            while True:
                quantity = user_input(f"Enter quantity of {result} book : ")
                decor_line()

                if quantity.isdigit() and int(quantity) < 0:
                    error_message("Please enter valid quantity !")
                else:
                    break

            wb = load_workbook(BOOK_DATA_PATH)
            s = wb.create_sheet(str(genre) + " -- " + str(new_code))
            header = ["Sr No","DDC Code","Book Name","Author Name","Language","Published Date","Wholesale Price","Market Price (INR)","Profit Margin","Quantities Available"]
            col_width = [7,15,50,28,17,20,18,21,20,25]
            f = Font(bold=True, underline="single")
            b = Border(left=Side("thin"),right=Side("thin"),top=Side("thin"),bottom=Side("thin"))
            pm = int(int(buy_price) * 30/100)
            wp = int(int(buy_price) - pm)

            for i in range(len(header)):
                col = i + 1
                c = s.cell(row=1, column=col)
                c.value = header[i]
                c.font = f
                c.alignment = Alignment(horizontal="center")
                c.border = b
                s.column_dimensions[c.column_letter].width = col_width[i]
            s.append([1,f"{new_code}10001",bookname,authorname,lang,publish_date,wp,int(buy_price),pm,int(quantity)])
            for cell in s[s.max_row]:
                cell.alignment = Alignment(horizontal='center', vertical='center')

            wb.save(BOOK_DATA_PATH)

        else:

            code_list,bookname_list,author_list,price_list,quantity_list,total_list = [],[],[],[],[],[]
            date = datetime.today().strftime('%d-%m-%Y')
    
            head_color("\n--- Add New Book ---\n")

            while True:

                display_genres()
                decor_line()
                genre = user_input(f"Enter exact genre code of desire book from above table : ").upper()
                decor_line()
                
                wd = load_workbook(BOOK_DATA_PATH)
                sheet = None
                for s in wd.sheetnames:
                    if genre in s:
                        sheet = s
                        break
                if sheet is None:
                    error_message("Genre Not Found!")
                    return
                    
                bookname = user_input(f"Enter proper name of book : ")
                decor_line()

                authorname = user_input(f"Enter author name of book : ")
                decor_line()
            
                lang = user_input(f"Enter language in which book is written : ").upper()
                decor_line()

                publish_date = user_input(f"Enter publish date of book in format 'dd-mm-yy': ")
                decor_line()

                while True:
                    buy_price = user_input(f"Enter price of book : ")
                    decor_line()

                    if buy_price.isdigit() and int(buy_price) < 0:
                        error_message("Please enter valid price !")
                    else:
                        break

                while True:
                    quantity = user_input(f"Enter quantity of book : ")
                    decor_line()

                    if not quantity.isdigit():
                        error_message("Please enter valid quantity !")

                    elif int(quantity) < 0:
                        error_message("Please enter valid quantity !")
                    else:
                        break

                ws = wd[sheet]
                last_row = ws.max_row
                last_sr = ws.cell(row=last_row,column=1).value
                last_uc = ws.cell(row=last_row,column=2).value
                new_sr = int(last_sr) + 1
                text,digt = "",""
                pm = int(int(buy_price) * 30/100)
                wp = int(int(buy_price) - pm)
                for i in last_uc:
                    if i.isdigit() == False:
                        text = text + i
                    else:
                        digt = digt + i
                new_digt = int(digt) + 1
                new_uc = text + str(new_digt)
                ws.append([new_sr,new_uc,bookname,authorname,lang,publish_date,wp,int(buy_price),pm,int(quantity)])

                for cell in ws[ws.max_row]:
                    cell.alignment = Alignment(horizontal='center', vertical='center')
                wd.save(BOOK_DATA_PATH)

                wb = load_workbook(BOOK_DATA_PATH)
                for s in wb.worksheets:
                    for row in s.iter_rows(min_row=2,values_only=False):
                        if str(row[1].value).strip() == str(new_uc):
                            code_list.append(row[1].value)
                            bookname_list.append(row[2].value)
                            author_list.append(row[3].value)
                            price_list.append(int(wp))
                            quantity_list.append(int(quantity))
                            total_list.append(int(int(wp) * int(quantity)))

                    break

                while True:
                    head_color("Want to add more book(s)?\n")
                    text_color("\t1.Yes")
                    text_color("\t2.No")

                    sel_option = ask_option_number()

                    if sel_option == "1":
                        break

                    elif sel_option == "2":
                        update_record(1,code_list,bookname_list,author_list,price_list,quantity_list,total_list,date)
                        correct_message("Data Updated Successfully!")
                        return

                    else:
                        option_error()
                        continue
                

                correct_message("Book Added Successfully!")



    def add_copies():
        head_color("\n--- Add Copies Of Books ---\n")

        code_list,bookname_list,author_list,price_list,quantity_list,total_list = [],[],[],[],[],[]
        date = datetime.today().strftime('%d-%m-%Y')
    


        while True:
            decor_line()
            unique_code = user_input("Enter unique code of book : ").upper()
            wb = load_workbook(BOOK_DATA_PATH)
            a = 0
            for sheet in wb.worksheets:
                for row in sheet.iter_rows(min_row=2,values_only=False):
                    if str(row[1].value).strip() == unique_code.upper():
                        code_list.append(row[1].value)
                        bookname_list.append(row[2].value)
                        author_list.append(row[3].value)
                        price_list.append(int(row[6].value))
                        a = 1
                        break

                if a == 1:
                    break

            if a == 1:
                correct_message(" Book Found with this unique code ")

                while True:
                    decor_line()
                    quantity = user_input("Enter quantity of copies of this book to be added : ")

                    if not quantity.isdigit():
                        error_message("Please enter valid quantity!")

                    elif int(quantity) > 0:
                        row[7].value = int(row[7].value) + int(quantity)
                        quantity_list.append(int(quantity))
                        total_list.append(int(row[6].value) * int(quantity))
                        wb.save(BOOK_DATA_PATH)
                        correct_message("Data updated successfully ! ")
                        decor_line()
                        break
                    else:
                        error_message(" Please enter valid quantity ! (ex. 2 or 4)")
            
            else:
                error_message("Book with this unique code not found !")


            while True:
                head_color("Want to add more book(s)?\n")
                text_color("\t1.Yes")
                text_color("\t2.No")

                sel_option = ask_option_number()

                if sel_option == "1":
                    break

                elif sel_option == "2":
                    update_record(1,code_list,bookname_list,author_list,price_list,quantity_list,total_list,date)
                    correct_message("Data Updated Successfully!")
                    return

                else:
                    option_error()
                    continue
            

    def add_old_book():
        decor_line()
        head_color("Actions Available :\n")
        text_color("\t1. Want to search Unique Code of book(s)?")
        text_color("\t2. Directly Add copies of book(s)")

        while True:
            decor_line()    
            sel_option = user_input("Enter option number from options : ")

            if sel_option == "1":
                search_book()
                break
            if sel_option == "2":
                add_copies()
                break
        
    def menu():
        decor_line()
        head_color("Actions Available :\n")
        text_color("\t1. Search Book(s)")
        text_color("\t2. Check Stock Balance")
        text_color("\t3. Add Copies of Available Book(s)")
        text_color("\t4. Add New Books(s)")
        text_color("\t5. Add New Genre")
        text_color("\t6. Exit")

        while True:
            decor_line()    
            select_option = user_input("Enter option number from options : ")

            if select_option == "1":
                search_book()
                menu()
                break

            elif select_option == "2":
                check_stock()
                menu()
                break

            elif select_option == "3":
                add_old_book()
                menu()
                break

            elif select_option == "4":
                add_new_book()
                menu()
                break

            elif select_option == "5":
                add_new_book("new")
                menu()
                break

            elif select_option == "6":
                break

            else:
                option_error()

    menu()

def fourth_p():

    sub_title("DIRECTOR CORNER")

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
                    with open(EMPLS_DATA_PATH, "r") as f:
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
            console.print(f"[#665D00]Hint : Your OTP is: {otp}[/]")                    
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
            with open(EMPLS_DATA_PATH, "r") as f:
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

            with open(CREDT_DATA_PATH, "a") as f:
                f.write(f"{new_emp_id} {usecode}\n")

            with open(EMPLS_DATA_PATH, "a", newline="\n") as file:
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

                with open(EMPLS_DATA_PATH, "r") as f:
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
                text_color("You can grant/revoke only one access at a time : \n")
                info_message("\t1. Cashier")
                info_message("\t2. Stock Clerk")
                info_message("\t3. Proprietor\n")

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

            with open(EMPLS_DATA_PATH, "r+", newline="") as f:
                rows = list(csv.reader(f))

                for row in rows:
                    while row and row[-1] == "":
                        row.pop()

                for row in rows:
                    if row[3] == pn:
                        if row and len(row) == 6 and result == "g":
                            d = 1
                            row.append(access)
                        elif row and len(row) == 7 and result == "g":
                            d = 1
                            if access not in row[6]:
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
                    write = csv.writer(f)
                    write.writerows(rows)
                    f.truncate()

                if d == 2:
                    error_message("Not accessed with any applications to revoke!")
                    return

                if d == 3:
                    error_message("Please ensure that employee has created username & password before granting/revoking any access!")
                    return

    def check_sales():

        profit1,profit2,profit3 = [],[],[]
        loss1,loss2,loss3 = [],[],[]
        d1,d2,d3 = [],[],[]
        t1,t2,t3 = [],[],[]

        date = datetime.today().strftime('%d-%m-%Y')

        wb = load_workbook(STORE_DATA_PATH)
        s = wb["Store Data"]
        for row in s.iter_rows(min_row=2,values_only=False):
            if str(row[6].value).strip() == str(date):
                loss1.append(int(row[5].value))
                d1.append(int(row[4].value))
            if str(row[6].value).strip()[3:] == str(date)[3:]:
                loss2.append(int(row[5].value))
                d2.append(int(row[4].value))
            if str(row[6].value).strip()[-2:] == str(date)[-2:]:
                loss3.append(int(row[5].value))
                d3.append(int(row[4].value))

        wd = load_workbook(STORE_DATA_PATH)
        s = wd["Users Data"]
        for row in s.iter_rows(min_row=2,values_only=False):
            for row in s.iter_rows(min_row=2,values_only=False):
                if str(row[7].value).strip() == str(date):
                    profit1.append(int(row[6].value))
                    t1.append(int(row[4].value))
                if str(row[7].value).strip()[3:] == str(date)[3:]:
                    profit2.append(int(row[6].value))
                    t2.append(int(row[4].value))
                if str(row[7].value).strip()[-2:] == str(date)[-2:]:
                    profit3.append(int(row[6].value))
                    t3.append(int(row[4].value))

        p1,p2,p3 = sum(profit1),sum(profit3),sum(profit3),
        l1,l2,l3 = sum(loss1),sum(loss2),sum(loss3)
        s1,s2,s3 = sum(t1),sum(t2),sum(t3)
        a1,a2,a3 = sum(d1),sum(d2),sum(d3)

        table = Table()
        header = ["NAME","TODAY","THIS MONTH","THIS YEAR"]
        for h in header:
            table.add_column(f"[green]{str(h)}[/]")
        table.add_row(f"[#0000ff]Total Books Sold[/]",str(s1),str(s2),str(s3))
        table.add_row(f"[#0000ff]Profit[/]",f"₹{str(p1)}",f"₹{str(p2)}",f"₹{str(p3)}")
        table.add_row(f"[#0000ff]Total Books Added[/]",str(a1),str(a2),str(a3))
        table.add_row(f"[#0000ff]Expense[/]",f"₹{str(l1)}",f"₹{str(l2)}",f"₹{str(l3)}")

        decor_line()
        console.print("\n[yellow]--Sale Of Store--[/]\n")
        console.print(table)

    def change_rate():
        wb = load_workbook(BOOK_DATA_PATH)
        for sheet in wb.sheetnames:
            s = wb[sheet]
            for row in s.iter_rows(min_row=2,values_only=False):
                if row[6].value is None:
                    continue
                row[6].value = int((int(row[7].value)) - int((int(row[7].value) * 30)/100))
                row[8].value = int((int(row[7].value) * 30)/100)
        wb.save(BOOK_DATA_PATH)  


    def menu():
        decor_line()
        head_color("Actions Available :\n")
        text_color("\t1. Search book(s)")
        text_color("\t2. Check sale of Store")
        text_color("\t3. Add New Employee")
        text_color("\t4. Grant Access to employee to applications")
        text_color("\t5. Revoke Access to employee to applications")
        text_color("\t6. Exit")

        while True:
            decor_line()    
            select_option = user_input("Enter option number from options : ")

            if select_option == "1":
                search_book()
                menu()
                break

            elif select_option == "2":
                check_sales()
                menu()
                break

            elif select_option == "3":
                add_new_employee()
                menu()
                break

            elif select_option == "4":
                grant_revoke_access("g")
                menu()
                break

            elif select_option == "5":
                grant_revoke_access("r")
                menu()
                break

            elif select_option == "6":
                return

            else:
                option_error()
    menu()

main_menu("WELCOME")
