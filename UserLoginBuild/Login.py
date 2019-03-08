import pyodbc
import os
import time
import MainMenu
import sys

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database\TestSystem.accdb;'
    )

try:
	cnxn = pyodbc.connect(conn_str)
	crsr = cnxn.cursor()
except (pyodbc.Error, pyodbc.OperationalError):
	print("No Driver Found!")
	input("")
	sys.exit()


def Login():
	title="Login - Route Manager"
	os.system("title "+title)
	global loginName
	os.system('cls')
	print("--- Login ---\n")
	loginName = input("Name: ")
	crsr.execute("select * from Users where Username=(?)", loginName)

	row = crsr.fetchone()
	if row:
		crsr.execute("select Password from Users where Username=(?)", loginName)
		lPass = input("Password: ")
		if lPass == row.Password:
			print("\nLogging in...")
			time.sleep(2)
			MainMenu.Menu(loginName)
		else: 
			print("Access Denied!")
			time.sleep(2)
			Login()
	else:
		print("Username not found!")
		input("")
		Login()

Login()
