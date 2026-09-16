#----------------    BACKEND    -----------------

#------------------------------------------------
# IMPORTANTS IMPORTS FOR THIS PROGRAM
#------------------------------------------------

import openpyxl
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment,Font,Border,Side
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

books_data_path = r"C:\Users\HP\Desktop\training\Python\Books_Store_Project\books_store\books_copy.xlsx"
users_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\users_data.xlsx"
empls_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\empls_data.csv"
credt_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\credentials.txt"

#------------------------------------------------
# PROGRAM START FROM HERE :
#------------------------------------------------

def add_books(result = ""):
    # wb = openpyxl.load_workbook(books_data_path)
    # for s in wb.sheetnames:
    #     sheet = wb[s]
        
    #     while True:
    #         genre = user_input("Enter Genre Of Book(s) : \n")
    #         for s in wb.sheetnames:
    #             if genre == str(s):
    #                 pass

    if result == "new":
            head_color("--- Add New Book ---\n")

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

            buy_price = user_input(f"Enter price of {result} book : ")
            decor_line()

            quantity = user_input(f"Enter quantity of {result} book : ")
            decor_line()

            wb = load_workbook(books_data_path)
            s = wb.create_sheet(str(genre) + " -- " + str(new_code))
            header = ["Sr No","DDC Code","Book Name","Author Name","Language","Published Date","Wholesale Price","Market Price (INR)","Profit Margin","Quantities Available"]
            col_width = [7,15,50,28,17,20,18,21,20,25]
            f = Font(bold=True, underline="single")
            a = Alignment(horizontal="center")
            b = Border(left=Side("thin"),right=Side("thin"),top=Side("thin"),bottom=Side("thin"))
            pm = int(int(buy_price) * 30/100)
            wp = int(int(buy_price) - pm)

            for i in range(len(header)):
                col = i + 1
                c = s.cell(row=1, column=col)
                c.value = header[i]
                c.font = f
                c.alignment = a
                c.border = b
                s.column_dimensions[c.column_letter].width = col_width[i]
            s.append([1,f"{new_code}10001",bookname,authorname,lang,publish_date,wp,int(buy_price),pm,int(quantity)])
            for cell in s[s.max_row]:
                cell.alignment = Alignment(horizontal='center', vertical='center')

            wb.save(books_data_path)

    else:
        decor_line()
        genre = user_input(f"Enter exact genre code of desire book from above table : ").upper()
        decor_line()
        
        wd = load_workbook(books_data_path)
        value = True
        for s in wd.sheetnames:
            if genre not in s:
                value = False
            else:
                value = True
                sheet = s
        if value == False:
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

        buy_price = user_input(f"Enter price of book : ")
        decor_line()

        quantity = user_input(f"Enter quantity of book : ")
        decor_line()

        req_s = None


        ws = wd[sheet]
        last_row = ws.max_row
        last_sr = ws.cell(row=last_row,column=1).value
        last_uc = ws.cell(row=last_row,column=2).value
        new_sr = int(last_sr) + 1
        text,digt = "",""
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
        wd.save(books_data_path)


decor_line()
head_color("Actions Available :\n")
text_color("\t1. Search book(s)")
text_color("\t2. Add book(s)")
text_color("\t3. Exit")

while True:
    decor_line()    
    select_option = user_input("Enter option number from options : ")

    if select_option == "1":
        search_book()
        break
    if select_option == "2":
        add_books("new")
        break

    if select_option == "3":
        break

    else:
        error_message("Please enter valid option nuber from above give options")
