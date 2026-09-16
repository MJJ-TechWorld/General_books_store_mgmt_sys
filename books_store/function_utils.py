import openpyxl
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from rich import console
from datetime import datetime, timedelta
from pyfiglet import figlet_format


import csv
import random
import time
import uuid
import os
import emoji

from getpass import getpass
from datetime import datetime, timedelta
from pyfiglet import figlet_format
from pyfiglet import Figlet

from rich.console import Console,Group
from rich.table import Table
from rich.text import Text
from rich.rule import Rule
from rich.align import Align
from rich import box
from rich.panel import Panel
from rich.progress import track
console = Console()

#------------------------------------------------
# ASSIGNING VALUES TO IMP VARIABLES :
#------------------------------------------------

empls_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\empls_data.csv"
books_data_path = r"C:\Users\HP\Desktop\training\Python\Books_Store_Project\books_store\books_copy.xlsx"

#------------------------------------------------
# DEFINING IMP FUNCTIONS OF DECORATIVE STUFFS :
#------------------------------------------------

def error_message(error):
    console.print(f"\n[bold red]⚠️ {error}[/bold red]\n")

def info_message(message):
    console.print(f"[green]{message}[/green]")

def correct_message(message):
    console.print(f"\n[bold cyan]✅ {message}[/]\n")

def decor_line():
    decor = "-"*80
    console.print(f"[#8A2BE2]{decor}[/#8A2BE2]")

def decor1_color(message):
    console.print(f"\n[bold underline #FFAA33]{message}[/]")

def head_color(message):
    console.print(f"\n[bold underline #FF8C00]{message}[/]")

def text_color(message):
    console.print(f"[#FF007F]{message}[/]")

def user_input(message):
    return console.input(f"[#FFBF00]{message}[/]").strip()

def ask_option_number():
    message = "Enter option number to proceed further : "
    return console.input(f"\n[#FFFF00]{message}[/]").strip()

def option_error():
    message = "Please enter valid option number from given options"
    error_message(message)

def progress_bar(val=1):
    for _ in track(range(30), description="Processing..."):
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

    with open(empls_data_path, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if (row and row[1] == username and access in row[5]):
                correct_message("Username Found")
                return "yes"
            
        error_message("Invalid Username!")


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
    with open(empls_data_path, "r") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            if (row and len(row)>1 and row[1] == u  and row[2] == p):
                correct_message("Logged in successfully!\n")
                return "yes"

        error_message("Wrong Password!\n")

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
            check_by_publish_date()
            return

        else:
            error_message("Please enter valid option number from given options")

def check_by_book_name():
    decor_line()
    value = False
    book_name = user_input("Enter name of book : ")
    decor_line()

    wb = load_workbook(books_data_path)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=True):
            if book_name in str(row[2]).strip().lower():
                info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                decor_line()
                value = True

    wb.save(books_data_path)

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

    wb = load_workbook(books_data_path)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=True):
            if author_name in str(row[3]).strip().lower():
                info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                decor_line()
                value = True

    wb.save(books_data_path)

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

    wb = load_workbook(books_data_path)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=True):
            if publish_date in str(row[5]).strip().lower():
                info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                decor_line()
                value = True

    wb.save(books_data_path)

    if value:
        decor_line()
        return
        
    else:
        error_message("Book Not Found!")

def display_genres():
    try : 
        # print(decor2, "\n")
        # print(decor2)
        wb = load_workbook(books_data_path)
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

        #     if sheet_names.index(i) % 2 == 0:
        #         table.add_row(i)
        #         # print(f"   {info_color}{i:<50}|", end = "")
        #     else:
        #         table.add_row(i)
        #         # print(f"{info_color}{i:>50}")

        # # print("\n", decor2)
        console.print(table)

    except FileNotFoundError:
        filenoterror()

def check_by_genre():
    display_genres()
    decor_line()
    value = False
    genre = user_input("Enter genre of desire book from above table : ").strip().lower()
    decor_line()


    wb = load_workbook(books_data_path, data_only=True)
    for s in wb.worksheets:
        if genre in str(s.title).strip().lower():
            for row in s.iter_rows(min_row=2, values_only=True ):
                info_message(f"{row[1]} : {row[2]} : {row[3]} : Avail {row[9]} : Price {row[7]}")
                decor_line()
                value = True

    wb.save(books_data_path)

    if value:
        decor_line()
    else:
        error_message("Book Not Found!")

def login_title():
    f = Figlet(font='small',width=250)
    title_box = Table(box=box.ROUNDED, border_style="#FFF3E0",style="on #2d1f0f",expand=True,show_header=False,padding=(1,2))
    title_box.add_column(justify="center", no_wrap=True)

    title_box.add_row(Align.center(Text(f.renderText("DIGITAL  BOOKS  STORE"),style="bold bright_white on #0F2D2E")))
    title_box.add_row(Align.center(Text("( By MJJ-TechWorld )",style="bold #FFD700")))

    console.print(title_box)

display_genres()