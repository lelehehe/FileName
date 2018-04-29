from pathlib import Path
import re

SE_REGEX = re.compile(r"[sS]\d{2}[eE]\d{2}")

videoPath = "/Volumes/Plex/Download/review/Criminal Minds/S01/test"
path = Path(videoPath)

def purge(fileName):
    newName = SE_REGEX.split(fileName)[0]
    print(' name=', newName)
    s01e01 = SE_REGEX.search(fileName).group().upper()
    print(', match=',  s01e01)
    return newName + s01e01


files = [p for p in Path(videoPath).iterdir() if p.is_file()]

for file in files: 
    # old name: file.stem
    #print(file.name, file.stem)
    stem = purge(file.stem)
    print(' stem=', stem)
    file.rename(Path(file.parent, stem + file.suffix))

