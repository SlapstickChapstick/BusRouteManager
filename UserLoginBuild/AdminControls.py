import pyodbc
import os
import RouteManager
import MainMenu

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database\TestSystem.accdb;'
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

def Menu(loginName):
	os.system('cls')
	print("--- Route Manager ---\n")
	
	print("\n1. Change Password\n2. Create User\n3. Delete User\n4. Back")
	option = int(input("\nOPTION: "))

	if option == 1:
		ChangePassword(loginName)
		
	elif option == 2:
		CreateUser(loginName)

	elif option == 3:
		DeleteUser(loginName)
	
	elif option == 4:
		MainMenu.Menu(loginName)

def ChangePassword(loginName):
	crsr.execute("SELECT * From Users WHERE Username=?", loginName)
	for rows in crsr.fetchall():
		if rows.Role == "Admin":
			userToChange = input("\nUser: ")
			crsr.execute("SELECT * FROM Users")
			newPassword = input("New Password: ")
			crsr.execute("UPDATE Users SET Password=(?) WHERE Username=(?)",newPassword,userToChange)
			cnxn.commit()
			input("")
			Menu(loginName)
		else:
			print("You do not have the required permissions.")
			input("")
			Menu(loginName)

def CreateUser(loginName):
	crsr.execute("SELECT * From Users WHERE Username=?", loginName)
	for rows in crsr.fetchall():
		if rows.Role == "Admin":
			newFName = input("\nFirst Name: ")
			newLName = input(" Last Name: ")
			newUName = input("  Username: ")
			newPassW = input("  Password: ")
			newURole = input("      Role: ")
			crsr.execute("INSERT INTO Users (FirstName,LastName,Username,Password,Role) VALUES(?, ?, ?, ?, ?)",newFName,newLName,newUName,newPassW,newURole)
			cnxn.commit()
			print("\nUser has been created!")
			input("")
			Menu(loginName)
		else:
			print("You do not have the required permissions.")
			input("")
			Menu(loginName)

def DeleteUser(loginName):
	crsr.execute("SELECT * From Users WHERE Username=?", loginName)
	for rows in crsr.fetchall():
		if rows.Role == "Admin":
			userToDel = input("\nUser to delete: ")
			crsr.execute("DELETE FROM Users WHERE Username=?",userToDel)
			cnxn.commit()
			print("User deleted!")
			input("")
			Menu(loginName)
		else:
			print("You do not have the required permissions.")
			input("")
			Menu(loginName)