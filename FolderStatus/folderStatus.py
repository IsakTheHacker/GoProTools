#Imports
import os

filesInDir = 0

#Arrays
thmFiles = []
lrvFiles = []
jpgFiles = []

h264Videos = []
h265Videos = []

nonGoProFiles = []

def printStats():
	print("\nContains {} useless files, of which {} are thm files and {} are drv files.".format(len(thmFiles) + len(lrvFiles), len(thmFiles), len(lrvFiles)))
	print("{} photos (jpg)".format(len(jpgFiles)))
	print("{} videos (mp4), of which {} use H.264 coding (AVC) and {} use H.265 coding (HEVC)".format(len(h264Videos) + len(h265Videos), len(h264Videos), len(h265Videos)))

for entry in os.scandir(os.path.abspath(os.getcwd())):
	if entry.is_dir():
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

	filesInDir += 1

print("Directory: \"{}\". {} total files!".format(os.path.abspath(os.getcwd()), filesInDir))
printStats()