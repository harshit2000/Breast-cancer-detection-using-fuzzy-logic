import cx_Freeze
import sys
import matlab.engine


base = None

if sys.platform == "win32":
	base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py",base=base, icon='icon.ico')]

cx_Freeze.setup(
	name="Fuzzy expert system",
	options={ "build_exe":{"packages":["tkinter","matlab.engine"],"include_files":["evalFuzzy.m","createOutputGraph.m","project.fis","output.jpg"]}	},
	version="0.1",
	description="Expert system to detect breast cancer",
	executables=executables
	)
