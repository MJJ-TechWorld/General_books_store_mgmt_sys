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
# PROGRAM START FROM HERE :
#------------------------------------------------

def add_books():
    wb = openpyxl.load_workbook(books_data_path)
    for s in wb.sheetnames:
        sheet = wb[s]
        
        while True:
            genre = user_input("Enter Genre Of Book(s) : \n")
            for s in wb.sheetnames:
                if genre == str(s):
                    pass

                    
            bookname = user_input("Enter proper name of book : \n")

            authorname = user_input("Enter author name of book : ")
        
            publish_date = user_input("Enter publish date of book : ")

            lang = user_input("Enter language in which book is written : ")

            buy_price = user_input("Enter price of book : ")


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
        add_books()
        break

    if select_option == "3":
        break

    else:
        error_message("Please enter valid option nuber from above give options")
