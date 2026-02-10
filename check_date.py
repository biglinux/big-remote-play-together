
import os
import datetime

path = '/usr/lib/libicuuc.so.76'
if os.path.exists(path):
    mtime = os.path.getmtime(path)
    dt = datetime.datetime.fromtimestamp(mtime)
    print(f"File: {path}")
    print(f"Last modified: {dt}")
    with open('file_date.txt', 'w') as f:
        f.write(str(dt))
else:
    print("File not found")
