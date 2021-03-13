#Imports
import os
import getpass

print("Will remove all LRV and THM files from \"{}\", is this OK?".format(os.path.abspath(os.getcwd())))

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