#Imports
import os

import colorama
from colorama import Fore
colorama.init()

totalItems = 0

#Arrays
thmFiles = []
lrvFiles = []
jpgFiles = []

h264Videos = []
h265Videos = []

nonGoProFiles = []
folders = []

def printStats():
	print("\nContains {}{}{} useless files, of which {}{}{} are thm files and {}{}{} are drv files.".format(
		Fore.BLUE, len(thmFiles) + len(lrvFiles), Fore.RESET,
		Fore.CYAN, len(thmFiles), Fore.RESET,
		Fore.CYAN, len(lrvFiles), Fore.RESET
	))
	print("{}{}{} photos (jpg)".format(
		Fore.MAGENTA, len(jpgFiles), Fore.RESET
	))
	print("{}{}{} videos (mp4), of which {}{}{} use H.264 coding (AVC) and {}{}{} use H.265 coding (HEVC)".format(
		Fore.MAGENTA, len(h264Videos) + len(h265Videos), Fore.RESET,
		Fore.CYAN, len(h264Videos), Fore.RESET,
		Fore.CYAN, len(h265Videos), Fore.RESET
	))
	print("\nNon GoPro stuff:")
	print("{}{}{} files".format(
		Fore.RED, len(nonGoProFiles), Fore.RESET
	))
	print("{}{}{} folders".format(
		Fore.RED, len(folders), Fore.RESET
	))

for entry in os.scandir(os.path.abspath(os.getcwd())):
	totalItems += 1

	if entry.is_dir():
		folders.append(entry.name)
		continue
		
	if entry.is_file() and entry.name.lower().endswith(".thm"):
		thmFiles.append(entry.name)
	elif entry.is_file() and entry.name.lower().endswith(".lrv"):
		lrvFiles.append(entry.name)
	elif entry.is_file() and entry.name.lower().endswith(".jpg"):
		jpgFiles.append(entry.name)
	elif entry.is_file() and entry.name.lower().endswith(".mp4"):
		if entry.name.lower().startswith("gh"):
			h264Videos.append(entry.name)
		elif entry.name.lower().startswith("gx"):
			h265Videos.append(entry.name)
	else:
		nonGoProFiles.append(entry.name)

print("Directory: {}\"{}\"{}. {}{}{} total items!".format(
	Fore.GREEN, os.path.abspath(os.getcwd()), Fore.RESET,
	Fore.YELLOW, totalItems, Fore.RESET
))
printStats()