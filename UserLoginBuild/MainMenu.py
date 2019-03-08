import RouteManager
import AdminControls
import os
import sys

def Menu(loginName):
		title="Menu - Route Manager [User: "+loginName+"]"
		os.system("title "+title)
		os.system('cls')
		print("--- Menu ---")
		print("\n1. Route Manager\n2. Control Panel\n3. Exit")

		try:
			option = int(input("\nOPTION: "))
		except ValueError:
			print()
			input("")

		if option == 1:
			RouteManager.RouteMenu(loginName)
		
		elif option == 2:
			AdminControls.Menu(loginName)

		elif option == 3:
			sys.exit(0)