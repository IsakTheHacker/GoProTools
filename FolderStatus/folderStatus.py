#Imports
import os

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
	print("\nContains {} useless files, of which {} are thm files and {} are drv files.".format(len(thmFiles) + len(lrvFiles), len(thmFiles), len(lrvFiles)))
	print("{} photos (jpg)".format(len(jpgFiles)))
	print("{} videos (mp4), of which {} use H.264 coding (AVC) and {} use H.265 coding (HEVC)".format(len(h264Videos) + len(h265Videos), len(h264Videos), len(h265Videos)))
	print("\nNon GoPro stuff:")
	print("{} files".format(len(nonGoProFiles)))
	print("{} folders".format(len(folders)))

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

print("Directory: \"{}\". {} total items!".format(os.path.abspath(os.getcwd()), totalItems))
printStats()