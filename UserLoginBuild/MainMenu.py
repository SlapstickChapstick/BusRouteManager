import RouteManager
import AdminControls
import os
import sys

def Menu(loginName):
		os.system('cls')
		print("--- Menu ---")
		print("\n1. Control Panel\n2. Route Manager\n3. Exit")

		try:
			option = int(input("\nOPTION: "))
		except ValueError:
			print()
			input("")

		if option == 1:
			AdminControls.Menu(loginName)
		
		elif option == 2:
			RouteManager.RouteMenu(loginName)

		elif option == 3:
			sys.exit()