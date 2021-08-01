#Imports
import os
import getpass

if __name__ == "__main__":
	print("Welcome to the LRV (Low Resolution Video) Patcher! This utility adds \".mp4\" to all LRV files in a folder you specify. This makes it possible to use the LRVs as proxies in your editing software.")
	ok = input("Do you want to add the \"mp4\" extension to all LRV files in your current folder? Yes/No: ")
	if (ok.lower() == "yes") or (ok.lower() == "y"):
		for entry in os.scandir(os.path.abspath(os.getcwd())):
			if entry.name.endswith(".LRV"):
				os.rename(entry.path, entry.path.replace("GL", "GX").replace(".LRV", ".mp4"))
	else:
		print("\nLRV Patcher was canceled!")

	getpass.getpass("Press ENTER to exit...")