#Imports
import os
import getpass

import colorama
from colorama import Fore
colorama.init()


def fileRemove():
	totalItems = 0

	#Arrays
	thmFiles = []
	lrvFiles = []

	for entry in os.scandir(os.path.abspath(os.getcwd())):
		totalItems += 1
		if entry.is_dir():
			continue

		if entry.is_file():
			if entry.name.lower().endswith(".thm"):
				thmFiles.append(entry.name)
			elif entry.name.lower().endswith(".lrv"):
				lrvFiles.append(entry.name)

	if len(thmFiles):
		print("{}{}{} thm files:\n{}".format(
			Fore.BLUE, len(thmFiles), Fore.RESET,
			"\n".join(thmFiles)
		))
	if len(lrvFiles):
		print("{}{}{} lrv files:\n{}".format(
			Fore.BLUE, len(lrvFiles), Fore.RESET,
			"\n".join(lrvFiles)
		))

	if not (len(thmFiles) or len(lrvFiles)):
		return True

	print("Will remove the files above from {}\"{}\"{}, is this OK?".format(
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

	return True

if __name__ == "__main__":
	fileRemove()
	
getpass.getpass("Press ENTER to exit...")