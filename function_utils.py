# import openpyxl
# from colorama import init, Fore, Back, Style
# init(autoreset=True)
# from openpyxl import load_workbook
# from openpyxl.styles import Alignment
# from rich import console
# from datetime import datetime, timedelta
# from pyfiglet import figlet_format


# import csv
# import random
# import time
# import uuid
# import os
# import emoji

# from getpass import getpass
# from datetime import datetime, timedelta
# from pyfiglet import figlet_format
# from pyfiglet import Figlet

# from rich.console import Console,Group
# from rich.table import Table
# from rich.text import Text
# from rich.rule import Rule
# from rich.align import Align
# from rich import box
# from rich.panel import Panel
# from rich.progress import track
# console = Console()

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

#------------------------------------------------
# ASSIGNING VALUES TO IMP VARIABLES :
#------------------------------------------------

CREDaT_DATA_PATH = "Credential.txt"
EMPLaS_DATA_PATH = "Employees_Data.csv"
BOOK_DATA_PATH = "BOOKS_DATA.xlsx"
STORE_DATA_PATH = "STORE_RECORDS.xlsx"
LOGa_DATA_PATH = "Activity_Log.txt"

# CREDT_DATA_PATH = r"books/store/Credential.txt"
# EMPLS_DATA_PATH = r"books_store/Employees_Data.csv"
# LOG_DATA_PATH = r"books_store/Activity_Log.txt"

CREDT_DATA_PATH = "CREDENTIAL.txt"
EMPLS_DATA_PATH = "EMPLOYEES.csv"
LOG_DATA_PATH = "Activity_Log.txt"

# emplyee = "EMPLOYEES.csv"
# cred = "CREDENTIAL.txt"


#------------------------------------------------
# DEFINING IMP FUNCTIONS OF DECORATIVE STUFFS :
#------------------------------------------------

def error_message(error):
    console.print(f"\n[bold red]⚠️  {error}[/bold red]\n")

def info_message(message):
    console.print(f"[green]{message}[/green]")

def correct_message(message):
    console.print(f"\n[bold cyan]✅ {message}[/]\n")

def decor_line():
    decor = "-"*80
    console.print(f"[#8A2BE2]{decor}[/#8A2BE2]")

def decor1_color():
    d = "*" * 80
    console.print(f"\n[#FFAA33]{d}[/]")

def head_color(message):
    console.print(f"\n[bold underline #FF8C00]{message}[/]")

def text_color(message):
    console.print(f"[#FF007F]{message}[/]")

def user_input(message):
    return console.input(f"[bold bright_blue]{message}[/]").strip()

def ask_option_number():
    message = "Enter option number to proceed further : "
    return console.input(f"\n[bold#FFFF00]{message}[/]").strip()

def option_error():
    message = "Please enter valid option number from given options"
    error_message(message)

def progress_bar(message,val=1):
    for _ in track(range(30), description=f"{message}..."):
            time.sleep(0.1)

def line(style="cyan"):
    return Rule(style=style)

def terminating_program():
    return text_color("---Program Terminated---\n")

def filenoterror():
    error_message("Please ensure that you had also cloned all data related folders from program link \n")
    terminating_program()

def filecloseerror():
    error_message("Please ensure that you have closed all excel files regarding this program !\n")
    terminating_program()


#------------------------------------------------
# DEFINING IMP FUNCTIONS USED IN PROGRAM ---
#------------------------------------------------

def check_username(username,access):
    """
    Check the username whether it is in record or not.
    Parameters: username : Username of employee who have access to this program.
                access : For checking whether employee has access to this.
    Returns: str: "yes" for correct username, "no" for wrong username. 
    """

    with open(EMPLS_DATA_PATH, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if (row and len(row) == 7 and row[4] == username and access in row[6]):
                return "yes"
            
        error_message("Invalid Username!")
        decor_line()


def check_password(u,p): 
    """
    Check the password whether it is in record with accordance with its username or not.
    Takes username & password as parameters and check accordingly.
    Args:
        u : Username of employee who have access to this program.
        p : Password of employee with registered username as well.
    Returns:
        str: "yes" for correct password, "no" for incorrect password.
    """
    with open(EMPLS_DATA_PATH, "r") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            if (row and len(row) == 7 and row[4] == u and row[5] == p):
                return "yes"

        error_message("Wrong Password!\n")
        decor_line()

# def create_data_excel():


def search_book():
    while True:
        decor_line()

        head_color("Available ways to search book(s) Or to check Unique Code of book(s):\n")
        text_color("\t1.By Name of Book -")
        text_color("\t2.By Name of Author of Book -")
        text_color("\t3.By Publishing Date of Book -")
        text_color("\t3.By Genre of Book -\n")

        sel_option = user_input("Enter option number to proceed further : ")

        if sel_option == "1":
            check_by_book_name()
            return

        if sel_option == "2":
            check_by_author_name()
            return

        if sel_option == "3":
            check_by_publish_date()
            return

        if sel_option == "4":
            check_by_genre()
            return

        else:
            error_message("Please enter valid option number from given options")

def check_by_book_name():
    decor_line()
    value = False
    book_name = user_input("Enter name of book : ")
    decor_line()

    wb = load_workbook(BOOK_DATA_PATH)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=True):
            if str(book_name).strip().lower() in str(row[2]).strip().lower():
                info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                decor_line()
                value = True

    wb.save(BOOK_DATA_PATH)

    if value:
        decor_line()
        return
    else:
        error_message("Book Not Found!")

def check_by_author_name():

    decor_line()
    value = False
    author_name = user_input("Enter author name of book : ")
    decor_line()

    wb = load_workbook(BOOK_DATA_PATH)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=True):
            if author_name in str(row[3]).strip().lower():
                info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                decor_line()
                value = True

    wb.save(BOOK_DATA_PATH)

    if value:
        decor_line()
        return
    else:
        error_message("Book Not Found!")

def check_by_publish_date():
    decor_line()
    value = False
    info_message("The date should be in format : dd-mm-yy \n")
    publish_date = user_input("Enter publishing date of book : ")
    decor_line()

    wb = load_workbook(BOOK_DATA_PATH)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=True):
            if publish_date in str(row[5]).strip().lower():
                info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                decor_line()
                value = True

    wb.save(BOOK_DATA_PATH)

    if value:
        decor_line()
        return
        
    else:
        error_message("Book Not Found!")

def display_genres():
    try :
        wb = load_workbook(BOOK_DATA_PATH)
        sheet_names = wb.sheetnames
        half = (len(sheet_names) + 1)//2
        left,right = sheet_names[:half],sheet_names[half:]

        table = Table(show_header=False,title=info_message("GENRES OF BOOKS AVAILABLE"),style="bold cyan")
    
        table.add_column(style="bright_magenta")
        table.add_column(style="bright_magenta")

        for i in range(half):
            l = left[i]
            if i < len(right):
                r = right[i]
            else:
                r = ""

            table.add_row(l,r)

        console.print(table)

    except FileNotFoundError:
        filenoterror()

def check_by_genre():
    display_genres()
    decor_line()
    genre = user_input(f"Enter exact genre code of desire book from above table : ").upper()
    decor_line()

    wb = load_workbook(BOOK_DATA_PATH)
    sheet = None
    for s in wb.sheetnames:
        if genre in s:
            sheet = s
            break

    if sheet is None:
        error_message("Genre Not Found!")
        return

    ws = wb[sheet]
    for row in ws.iter_rows(min_row=2, values_only=True ):
        decor_line()
        info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
        decor_line()

    wb.save(BOOK_DATA_PATH)
            
def check_stock():

    head_color("\n--- Check Stock Balance ---\n")

    while True:
        r = 0
        q = user_input("Enter quantity of books to be checked, left in store : ")
        if q.isdigit() and int(q) >= 0:
            head_color(f"\nBooks with {q} quantities left : ")
            wb = load_workbook(BOOK_DATA_PATH)
            for sheet in wb.worksheets:
                for row in sheet.iter_rows(min_row=2,values_only=False):
                    if str(row[9].value).strip() == str(q):
                        decor_line()
                        info_message(f"{row[1].value}  {row[2].value}  By {row[3].value}  Avail : {row[9].value}")
                        r = 1
            if r == 1:
                decor_line()
                break
            else:
                error_message("Please enter valid quantity !")


def main_title():
    f = Figlet(font='small',width=250)
    title_box = Table(box=box.ROUNDED, border_style="#FFF3E0",style="on #2d1f0f",expand=True,show_header=False,padding=(1,2))
    title_box.add_column(justify="center", no_wrap=True)

    title_box.add_row(Align.center(Text(f.renderText("DIGITAL  BOOKS  STORE"),style="bold bright_white on #0F2D2E")))
    title_box.add_row(Align.center(Text(f"⁓⁓"*50,style="#FFF3E0 on #2d1f0f")))
    title_box.add_row(Align.center(Text("( By MJJ-TechWorld )",style="bold #FFD700")))

    console.print(title_box)

def login_portal(access):
    title_box = Table(box=box.DOUBLE_EDGE, border_style="#FF007F",style="on #2d1f0f",expand=True,show_header=False,padding=(2,3))
    title_box.add_row(Text("LOGIN PORTAL",style="#0066FF",justify="center"))
    decor1_color()
    console.print(title_box)
    head_color("Username\n")

    while True:
        username = user_input("Enter Your Username : ")
        decor_line()

        if check_username(username,access) == "yes": 
            head_color("Password\n")
            while True:
                console.print("[bold bright_blue]Enter Your Password : [/]", end = "")
                password = pwinput.pwinput(prompt="", mask="*")
                decor_line()

                if check_password(username,password) == "yes":
                    info_message("Logged in successfully!")
                    decor_line()
                    progress_bar("Creating UI and required display")
                    decor1_color()
                    print("\n")
                    return username,password



def login_activity(u,p,a,s="Logged in"):

    with open(EMPLS_DATA_PATH, "r") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            if (row and row[4] == u and row[5] == p):
                id = row[0]
                fn = row[1]
                ln = row[2]
                name = fn + " " + ln
                Time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            
            if a == "c":
                action = "Cashier Corner"
            elif a == "s":
                action = "Stock Clerk Corner"
            elif a == "p":
                action = "Director Corner"

        
            with open(LOG_DATA_PATH, "a") as f:
                f.write(f"{id} - {name} - {s} - {action} - {Time}\n")

def menu_title(title):
    if title == "WELCOME":
        main_title()
        title_box = Table(box=box.DOUBLE_EDGE, border_style="#FF007F",style="on #2d1f0f",expand=True,show_header=False,padding=(1,1))
        title_box.add_row(Text(f"{title}",style="#0066FF",justify="center"))
        print("\n")
        console.print(title_box)
        print("\n")
    else:
        title_box = Table(box=box.DOUBLE_EDGE, border_style="#FF007F",style="on #2d1f0f",expand=True,show_header=False,padding=(1,1))
        title_box.add_row(Text(f"{title}",style="#0066FF",justify="center"))
        print("\n")
        console.print(title_box)
        print("\n")


def sub_title(title):

    title_box = Table(box=box.DOUBLE_EDGE, border_style="#FFF3E0",style="on #2d1f0f",expand=True,show_header=False,padding=(2,3))
    title_box.add_row(Text(f"{title}",style="#0066FF",justify="center"))
    print("\n")
    console.print(title_box)
    print("\n")

def Title():
    f = Figlet(font='small',width=250)
    title_box = Table(box=box.ROUNDED, border_style="#FF1493",style="on #1A020F",expand=True,show_header=False,padding=(1,2))
    title_box.add_column(justify="center", no_wrap=True, style="on #2D2327")

    title_box.add_row(Align.center(Text(f.renderText("DIGITAL  BOOKS  STORE"),style="bold bright_white on #0F2D2E")))
    title_box.add_row(Align.center(Text(f"⁓⁓"*50,style="#FF1493 on #340C20")))
    title_box.add_row(Align.center(Text("( By MJJ-TechWorld )",style="bold #FFD700")))

    console.print(title_box)
    print("\n")

def create_imp_files():

    if not os.path.exists(STORE_DATA_PATH):

        workbook = openpyxl.Workbook()

        sheet1 = workbook.active
        sheet1.title = "Users Data"

        header1 = ["Unique Code", "Book Name", "Author Name", "MRP (in Rs)", "Quantity", "Total", "Profit", "Date"]
        column_width1 = [20,52,34,19,18,19,22,17]

        for i in range(len(header1)):
            col = i + 1
            c = sheet1.cell(row=1, column=col)
            c.value = header1[i]
            c.font = Font(bold=True, underline="single")
            c.alignment = Alignment(horizontal="center")
            c.border = Border(left=Side("thin"),right=Side("thin"),top=Side("thin"),bottom=Side("thin"))
            sheet1.column_dimensions[c.column_letter].width = column_width1[i]

        sheet2 = workbook.create_sheet(title="Store Data")

        header2 = ["Unique Code", "Book Name", "Author Name", "Wholesale Price", "Quantity", "Total Expense", "Date"]
        column_width2 = [20,52,34,19,18,22,17]


        for i in range(len(header2)):
            col = i + 1
            c = sheet2.cell(row=1, column=col)
            c.value = header2[i]
            c.font = Font(bold=True, underline="single")
            c.alignment = Alignment(horizontal="center")
            c.border = Border(left=Side("thin"),right=Side("thin"),top=Side("thin"),bottom=Side("thin"))
            sheet2.column_dimensions[c.column_letter].width = column_width2[i]

        workbook.save(STORE_DATA_PATH)
        workbook.close()

    if not os.path.exists(EMPLS_DATA_PATH):
        header = [ ["EMP ID","First Name","Last Name","Phone Number","Username","Password","Access"],
        ["EMP101","New","User","1010101010","user@","12345678","csp"] ]

        with open(EMPLS_DATA_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(header)

    if not os.path.exists(CREDT_DATA_PATH):
        data = "EMP ID, Code\n"
        with open(CREDT_DATA_PATH, "w") as f:
            f.write(data)

    if not os.path.exists(LOG_DATA_PATH):
        data = "EMP ID - Name - Action - Session - Time\n"
        with open(LOG_DATA_PATH, "w") as f:
            f.write(data)

def display_log():

    decor_line()
    console.print("[blue] --- LOG DISPLAY --- ")
    decor1_color()
    with open(LOG_DATA_PATH, "r") as f:
        data = f.read()
        console.print(f"[#FFD54F]{data}[/]")

def update_record(sheet,code_list,bookname_list,author_list,price_list,quantity_list,total_list,date):

    wb = load_workbook(STORE_DATA_PATH)

    if sheet == 0:
        s = "Users Data"
        ws = wb[s]
        for i in range(len(code_list)):
            p = int((total_list[i]) * 30/100)
            ws.append([code_list[i],bookname_list[i],author_list[i],int(price_list[i]),int(quantity_list[i]),int(total_list[i]),p,date])
        for cell in ws[ws.max_row]:
            cell.alignment = Alignment(horizontal='center', vertical='center')

    else:
        s = "Store Data"
        ws = wb[s]
        for i in range(len(code_list)):
            ws.append([code_list[i],bookname_list[i],author_list[i],int(price_list[i]),int(quantity_list[i]),int(total_list[i]),date])
        for cell in ws[ws.max_row]:
            cell.alignment = Alignment(horizontal='center', vertical='center')

    wb.save(STORE_DATA_PATH)