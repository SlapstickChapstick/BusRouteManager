import pyodbc
import os
import MainMenu
from prettytable import PrettyTable

tbl = PrettyTable()

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database\TestSystem.accdb;'
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

def RouteMenu(loginName):
	os.system('cls')
	print("--- Route Manager ---\n")
	print("1. View Routes\n2. Add Route\n3. Assign Vehicle\n4. Change Route Status\n5. Exit Route Manager\n")
	option = int(input("OPTION: "))
	
	if option == 1:
		ViewRoutes(loginName)

	elif option == 2:
		AddRoute(loginName)

	elif option == 3:
		AssignBus(loginName)

	elif option == 4:
		ChangeStatus(loginName)

	elif option == 5:
		MainMenu.Menu(loginName)

def ViewRoutes(loginName):
	os.system('cls')
	crsr.execute("SELECT * FROM Routes")
	tbl.field_names = ["Route ID","Start","End","Bus Reg","Status"]
	
	for rows in crsr.fetchall():
		tbl.add_row([rows.RouteID,rows.StartPoint,rows.EndPoint,rows.BusReg,rows.Status])

	tbl.padding_width = 2
	print(tbl)

	input("")
	RouteMenu(loginName)

def AddRoute(loginName):
	os.system('cls')
	crsr.execute("select * from Routes")
	routeStart = input("Start Location: ")
	routeEnd = input("  End Location: ")
	routeReg = "Not Assigned"
	crsr.execute("INSERT INTO Routes (StartPoint, EndPoint)  VALUES(?,?)",routeStart,routeEnd)
	cnxn.commit()
	input("")
	RouteMenu(loginName)

def AssignBus(loginName):
	routeID = input("\nRoute ID: ")
	assignReg = input("Reg Number: ")
	crsr.execute("UPDATE Routes SET BusReg=(?) WHERE RouteID=(?)",assignReg,routeID)
	print("\nVehicle Assigned!")
	cnxn.commit()
	input("")
	RouteMenu(loginName)

def ChangeStatus(loginName):
	routeID = input("\nRoute ID: ")
	choice = int(input("\n1. Active\\n2. Inactive"))
	if choice == 1:
		crsr.execute("UPDATE Routes SET Status='Active' WHERE RouteID=(?)",routeID)
		print("\nStatus Changed!")
		cnxn.commit()
		input("")
		RouteMenu(loginName)
	elif choice == 2:
		crsr.execute("UPDATE Routes SET Status='Inactive' WHERE RouteID=(?)",routeID)
		print("\nStatus Changed!")
		cnxn.commit()
		input("")
		RouteMenu(loginName)
