#----------------    BACKEND    -----------------

#------------------------------------------------
# IMPORTANTS IMPORTS FOR THIS PROGRAM
#------------------------------------------------

import openpyxl
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from rich import console
from datetime import datetime, timedelta
from pyfiglet import figlet_format
from pyfiglet import Figlet
import pyfiglet



import csv
import random
import time
import uuid
import os
import emoji

from getpass import getpass
from datetime import datetime, timedelta
from pyfiglet import figlet_format

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

books_data_path = r"C:\Users\HP\Desktop\training\Python\books_store\books_copy.xlsx"
users_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\users_data.xlsx"
empls_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\empls_data.csv"
credt_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\credentials.txt"

#------------------------------------------------
# ASSIGNING VALUES TO IMP VARIABLES :
#------------------------------------------------


#------------------------------------------------
# DEFINING IMP FUNCTIONS OF DECORATIVE STUFFS :
#------------------------------------------------


#------------------------------------------------
# PROGRAM START FROM HERE :
#------------------------------------------------

# DEFINING IMP FUNCTIONS USED IN THIS PROGRAM ---

def display_login_title():
    pass



    # while True:
    #     username = input("Enter Your Username : ")



def create_bill(code,bookname,author,price,quantity,total):

    good_quotes = ["'Books are uniquely portable magic'",
                "'Today a reader,tomorrow a leader'",
                "'Read what you love until you love to read'"
                "'There is no friend as loyal as a book'",
                "'A book dream is a dream that you hold in your hand'"]
    quote = random.choice(good_quotes)

    Total = 0
    for i in total:
        Total = Total + int(i)
    date = datetime.today().strftime('%d-%m-%Y')
    decor_line()
    title_box = Table(box=box.ROUNDED, border_style="#FFF3E0",style="on #2d1f0f",expand=True,show_header=False,padding=(1,1))
    title_box.add_column(justify="center")
    title_box.add_row(Text("📚   DIGITAL LIBRARY OF NAVI MUMBAI   📚",style="bold bright_white on #0066FF",justify="center"))
    title_box.add_row(Text("( By MJJ-TechWorld )",style="bold #FFD700 on #1a1a1a",justify="center"))

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
    console.print(Panel(content, box=box.DOUBLE, border_style="#00BFFF on #D6EAFF",padding=(1,1), width=console.width - 2))
    
def buy_book():
    code_list,bookname_list,author_list,price_list,quantity_list,total_list = [],[],[],[],[],[]
    while True:
        value = False
        decor_line()
        head_color("---Buy Book(s)---\n")
        uc = user_input("Enter Unique Code Of Book : ").upper()
        wb = load_workbook(books_data_path)
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

        wb.save(books_data_path)

        if value:
            while True:
                value = False
                quantity = user_input("Enter quantity of this book : ")
                if int(quantity) <= int(avail_q) :
                    correct_message("Book Sold Successfully!")

                    code_list.append(uc)
                    bookname_list.append(bookname)
                    author_list.append(author)
                    price_list.append(price)
                    quantity_list.append(quantity)
                    total_list.append(int(price)*int(quantity))
                    
                    wb = load_workbook(books_data_path)
                    for sheet in wb.sheetnames:
                        s = wb[sheet]
                        for row in s.iter_rows(min_row=2,values_only=False):
                            if row[1].value == uc:
                                row[9].value = int(row[9].value) - int(quantity)
                    wb.save(books_data_path)

                    while True:
                        head_color("Want to buy more book(s)?\n")
                        text_color("\t1.Yes")
                        text_color("\t2.No")

                        sel_option = ask_option_number()

                        if sel_option == "1":
                            break

                        elif sel_option == "2":
                            create_bill(code_list,bookname_list,author_list,price_list,quantity_list,total_list)
                            break

                        else:
                            option_error()
                    break
                elif int(quantity) <= 0:
                    error_message("Please enter valid quantity")
                else:
                    error_message("Insufficient quantity of book available!")
        else:
            error_message("Book Not Found!") 


def choose_option():
    while True:
        decor_line()
        head_color("Available Options :\n")

        info_message("\t1. Want to check unique code of book once ?")
        info_message("\t2. Buy book(s) directly\n")

        sel_option = user_input("Enter option number to proceed further : ")

        if sel_option == "1":
            search_book()
            break

        elif sel_option == "2":
            buy_book()
            break
        else:
            error_message("Please enter valid option number from given options!")


def change_rate():
    wb = load_workbook(books_data_path)
    for sheet in wb.sheetnames:
        s = wb[sheet]
        for row in s.iter_rows(min_row=2,values_only=False):
            if row[6].value is None:
                continue
            row[6].value = int((int(row[7].value)) - int((int(row[7].value) * 30)/100))
            row[8].value = int((int(row[7].value) * 30)/100)
    wb.save(books_data_path)  




# wb = load_workbook(books_data_path)
# for sheet in wb.sheetnames:
#     s = wb[sheet]
#     for row in s.iter_rows(min_row=2,values_only=False):
#         if row[9].value is None:
#             continue

#         if isinstance(row[9].value, (int,float)) and row[9].value < 0:
#             row[9].value = abs(row[9].value)

#         if row[9].value < 0:
#             row[9].value = 5

#         if row[9].value == 0:
#             row[9].value = 4

#         if row[9].value == 1:
#             row[9].value = 6

#         if row[9].value == 2:
#             row[9].value = 3

# wb.save(books_data_path)

def banner():
    name = figlet_format('Digital Books\n Store',font="mini", width=200).strip()
    content = Group(
        Align.center(Text(name, style="bold bright_white on #00ACC1")),
        Text(""),
        Align.center(Text(" ( By MJJ-TechWorld ) ", style="bold #FFD700 on #3a3200"))
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

if __name__ == "__main__":
    banner()
    print(emoji.emojize(":earth_asia:"))
    print(emoji.emojize(":open_book:"))
    print(emoji.emojize(":books:"))
    print(emoji.emojize(":laptop:"))
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
            break
        elif select_option == "2":
            buy_book()
            break

        elif select_option == "3":
            break

        else:
            error_message("Please enter valid option nuber from above give options")

   
