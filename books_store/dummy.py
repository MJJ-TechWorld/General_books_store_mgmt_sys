# import csv
# import os


# CREDT_DATA_PATH = "Credential.txt"
# EMPLS_DATA_PATH = "Employees_Data.csv"
# LOG_DATA_PATH = "Activity_Log.txt"

# emplyee = "EMPLOYEES.csv"
# cred = "CREDENTIAL.txt"

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


# emp_id = "EMP102"
# emp_first_name = "an"
# emp_last_name = "addn"
# emp_mob_no = "1010102030"
# username = "as"
# password = "alalalalal"
# usecode = "342285bb2a8cadef22f667eeb6a6bjdw"

# with open(cred, "a") as f:
#     f.write(f"{emp_id} {usecode}\n")

# with open(emplyee, "a", newline="\n") as file:
#     write = csv.writer(file)
#     write.writerow([emp_id,emp_first_name,emp_last_name,emp_mob_no])


# with open(emplyee, "r+", newline="") as f:
#     data = csv.reader(f)
#     rows = []
#     for row in data:

#         if row[0] == emp_id and row[3] == emp_mob_no and len(row) == 4:
#             row.append(username)
#             row.append(password)

#         else:
#             print("Account Already Exists!")

#         rows.append(row)

#     f.seek(0)
#     writer = csv.writer(f)
#     for r in rows:
#         writer.writerow(r)

#     f.truncate()
