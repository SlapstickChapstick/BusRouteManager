import pyodbc
import os
import MainMenu

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
	print("    Route ID        Start           End      Bus Reg     Status")
	print("------------------------------------------------------------------------")
	for rows in crsr.fetchall():
		print("\t",rows.RouteID,"\t",rows.StartPoint,"\t",rows.EndPoint,"    ",rows.BusReg,"\t", rows.Status)

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
	choice = int(input("\n1. Active\2. Inactive"))
	if choice:
		crsr.execute("UPDATE Routes SET BusReg=(?) WHERE RouteID=(?)",routeID)
		print("\nVehicle Assigned!")
		cnxn.commit()
		input("")
		RouteMenu(loginName)
