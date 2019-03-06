import pyodbc
import os

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=S:\Olly Chapman - Apprenticeship\Assignments\Programs\TestSystem.accdb;'
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

def RouteMenu():
	os.system('cls')
	print("--- Route Manager ---\n")
	print("1. View Routes\n2. Add Route\n3. Assign Driver\n4. Exit Route Manager\n")
	option = int(input("OPTION: "))
	
	if option == 1:
		ViewRoutes()

	elif option == 2:
		AddRoute()

	elif option == 3:
		AssignDriver()

	elif option == 4:
		input("")

def ViewRoutes():
		os.system('cls')
		crsr.execute("SELECT * FROM Routes")
		print("    Route ID        Start           End          Bus Reg")
		print("-----------------------------------------------------------")
		for rows in crsr.fetchall():
			print("\t",rows.RouteID,"\t",rows.StartPoint,"\t",rows.EndPoint,"\t",rows.BusReg,"\t")

		input("")
		RouteMenu()

def AddRoute():
		os.system('cls')
		crsr.execute("select * from Routes")
		routeStart = input("Start Location: ")
		routeEnd = input("  End Location: ")
		routeReg = "Not Assigned"
		crsr.execute("INSERT INTO Routes (StartPoint, EndPoint)  VALUES(?,?)",routeStart,routeEnd)
		cnxn.commit()
		input("")
		RouteMenu()

def AssignDriver():
		os.system('cls')
		routeID = input("Route ID: BR-")
		crsr.execute("SELECT * FROM Routes WHERE RouteID=?",routeID)
		for rows in crsr.fetchall():
			print(rows)

