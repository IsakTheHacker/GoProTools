#Imports
import os
import getpass

import colorama
from colorama import Fore
colorama.init()

print("Will remove all {}LRV{} and {}THM{} files from {}\"{}\"{}, is this OK?".format(
	Fore.CYAN, Fore.RESET,
	Fore.CYAN, Fore.RESET,
	Fore.GREEN, os.path.abspath(os.getcwd()), Fore.RESET
))

ok = input("Yes/No: ")
if (ok.lower() == "yes") or (ok.lower() == "y"):
	print("\nRemoving files...")

	pathString = ""
	for entry in os.scandir(os.path.abspath(os.getcwd())):
		if entry.is_dir():
			continue

		if entry.is_file() and (entry.name.lower().endswith(".thm") or entry.name.lower().endswith(".lrv")):
			pathString += entry.name + "\n"
			os.remove(entry.path)

	print("Removed these files:")
	print(pathString)
else:
	print("\nUnnecessary file remove was canceled!")
	
getpass.getpass("Press ENTER to exit...")