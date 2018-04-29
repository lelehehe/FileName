from pathlib import Path
import re

SE_REGEX = re.compile(r"[sS]\d{2}[eE]\d{2}")

videoPath = "/Volumes/Plex/Download/review/Criminal Minds/S01/test"
path = Path(videoPath)

def rename(fileNameLelehehe1
    ):
    newName = SE_REGEX.split(fileName)
    print(newName)


files = [p for p in Path(videoPath).iterdir() if p.is_file()]

for file in files: 
    # old name: file.stem
    #print(file.name, file.stem)
    rename(file.stem)


