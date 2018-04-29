from pathlib import Path
import re

SE_REGEX = re.compile(r"[sS]\d{2}[eE]\d{2}")

videoPath = "/Volumes/Plex/Download/review/Criminal Minds/S01"
path = Path(videoPath)


files = [p for p in Path(videoPath).iterdir() if p.is_file()]

# private functions
def purge(fileName):
    found = SE_REGEX.search(fileName)
    if found is None: return None
    s01e01 = found.group().upper()
    print(', match=',  s01e01)
    newName = SE_REGEX.split(fileName)[0]
    print(' name=', newName)
    return newName + s01e01

for file in files: 
    # old name: file.stem
    print(file.name)
    stem = purge(file.stem)
    if stem is not None: 
        print('rename ', file.stem, ' to ', stem)
        if (file.suffix == '.ass' or file.suffix == '.srt'):
            suffix = ('.chs'+file.suffix)
        else:
            suffix = file.suffix
        print(' suffix=', suffix)
        file.rename(Path(file.parent, stem + suffix))




