from cx_Freeze import setup, Executable

base = None

executables = [Executable("Login.py", base=base)]

packages=["idna","pyodbc","os","time","sys"]
options = {
	'build_exe': {
		'packages':packages,
		},
	}

setup(
	name="Bus Manager",
	options = options,
	version = "v1.0.0a",
	description="A Python Bus Manager",
	executables = executables
)
