import pyodbc
import os
import time
import MainMenu
import sys

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=S:\Olly Chapman - Apprenticeship\Assignments\Programs\TestSystem.accdb;'
    )

try:
	cnxn = pyodbc.connect(conn_str)
	crsr = cnxn.cursor()
except (pyodbc.Error, pyodbc.OperationalError):
	print("No Driver Found!")
	input("")
	sys.exit()


def Login():
	global loginName
	os.system('cls')
	print("--- Login ---")
	loginName = input("Name: ")
	crsr.execute("select * from Users where Username=(?)", loginName)

	for row in crsr.fetchall():
		if not row:
			print("Username Not Found!")
			input("")
			Login()

		crsr.execute("select Password from Users where Username=(?)", loginName)
		lPass = input("Password: ")
		if lPass == row.Password:
			print("Access Granted!")
			MainMenu.Menu(loginName)
		else: 
			print("Access Denied!")
			time.sleep(2)
			Login()

Login()
