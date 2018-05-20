from pathlib import Path
import re
import os
from os import listdir
from os.path import isfile, join
from os import walk

SE_REGEX = re.compile(r"[sS]\d{2}[eE]\d{2}")

videoPath = "/Volumes/Plex/Download/new/Curb.Your.Enthusiasm"
path = Path(videoPath)

displayOnly = False

files = [p for p in Path(videoPath).iterdir() if p.is_file()]

if not files: 
    paths = [p for p in Path(videoPath).iterdir()]
    for path in paths:
        filesInSub = [p for p in Path(path).iterdir() if p.is_file()]
        files.extend(filesInSub)

# private functions
def purge(fileName):
    found = SE_REGEX.search(fileName)
    if found is None: return None
    s01e01 = found.group().upper()
    # print(', match=',  s01e01)
    newName = SE_REGEX.split(fileName)[0].replace(" ", "")
    if not newName.endswith('.'): 
        newName += '.'
    # print(' name=',newName, " final=", newName + s01e01)
    return newName + s01e01

for file in files: 
    # old name: file.stem
    stem = purge(file.stem)
    if stem is not None: 
        print('rename ', file.stem, ' to ', stem)
        if (file.suffix == '.ass' or file.suffix == '.srt'):
            suffix = ('.chs'+file.suffix)
        else:
            suffix = file.suffix
        # print(' suffix=', suffix)
        if not displayOnly:
            file.rename(Path(file.parent, stem + suffix))




